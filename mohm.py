import time
import json
import wiringpi as wp
import mohm_definitions
from mohm_definitions import *
from ADS1256_definitions import *
from pipyadc import ADS1256

ads = ADS1256()

# Definitions
TEMPERATURE_CHANNEL = (POS_AIN0 | NEG_AIN1)
RESISTANCE_CHANNELS_20_VOLTAGE_GAIN = (POS_AIN4 | NEG_AIN5, POS_AIN6 | NEG_AIN7)
RESISTANCE_CHANNELS_1000_VOLTAGE_GAIN = (POS_AIN2 | NEG_AIN3, POS_AIN6 | NEG_AIN7)


class OHMIMETRO(object):

    def __init__(self, conf=mohm_definitions):
        # Set up the wiringpi object to use physical pin numbers
        wp.wiringPiSetupPhys()
        # Config and initialize the SPI and GPIO pins used by the ADC.
        # The following four entries are actively used by the code:
        self.ESC1_PIN = conf.ESC1_PIN
        self.ESC2_PIN = conf.ESC2_PIN
        self.ESC3_PIN = conf.ESC3_PIN
        self.GAIN_PIN = conf.GAIN_PIN

        # GPIO Outputs. Only the CS_PIN is currently actively used. ~RESET and 
        # ~PDWN must be set to static logic HIGH level if not hardwired:
        for pin in (conf.ESC1_PIN,
                    conf.ESC2_PIN,
                    conf.ESC3_PIN,
                    conf.GAIN_PIN):
            if pin is not None:
                wp.pinMode(pin, wp.OUTPUT)
                wp.digitalWrite(pin, wp.LOW)

    def range_select(self, scale):
        scale = str(scale)
        # (1000 gain bit, scale bit 2, scale bit 1, scale bit 0)
        selected_bits = {
            '0': (0, 0, 0, 0),
            '1': (1, 0, 0, 1),
            '2': (0, 0, 0, 1),
            '3': (0, 0, 1, 0),
            '4': (0, 0, 1, 1),
            '5': (0, 1, 0, 0),
            '6': (0, 1, 0, 1),
            '7': (0, 1, 1, 0),
            '8': (0, 1, 1, 1),
        }
        output_bits = selected_bits.get(scale, (0, 0, 0, 0))

        wp.digitalWrite(self.ESC1_PIN, output_bits[3])
        wp.digitalWrite(self.ESC2_PIN, output_bits[2])
        wp.digitalWrite(self.ESC3_PIN, output_bits[1])
        wp.digitalWrite(self.GAIN_PIN, output_bits[0])

    def ads_calib(self):
        # Gain and offset self-calibration
        ads.cal_self()

    # compensates the each shunt and the INA's fixed gain
    def hw_gain_per_scale(self, escala):
        escala = str(escala)
        # (shunt value, current reading gain)
        ganhos_escala = {
            '0': (0, 0),
            '1': (1, 1000),
            '2': (1, 20),
            '3': (2, 20),
            '4': (20, 20),
            '5': (200, 20),
            '6': (2000, 20),
            '7': (20000, 20),
            '8': (200000, 20),
        }
        return ganhos_escala.get(escala, (0, 0))

    # compensates the each shunt and the INA's fixed gain
    def set_data_rate(self, data_rate):
        data_rate = str(data_rate)
        rate_options = {
            '0': DRATE_2_5,
            '1': DRATE_5,
            '2': DRATE_10,
            '3': DRATE_15,
            '4': DRATE_25,
        }

        ads.drate = rate_options.get(data_rate, DRATE_2_5)

    # Resistance measurement routine
    def do_measurement(self, scale, data_rate, stabilization, acquisitions):
        
        # Config data acquisition rate
        self.set_data_rate(data_rate)

        # Select the ohmmeters measurement range
        self.range_select(scale)

        # Define the proper Ina146 hardware gain
        hw_gain = self.hw_gain_per_scale(scale)
        
        # Stabilization time
        time.sleep(stabilization)

        # select which gain should be used
        if scale != 0x01:
            resistance_channels = RESISTANCE_CHANNELS_20_VOLTAGE_GAIN
        else:
            resistance_channels = RESISTANCE_CHANNELS_1000_VOLTAGE_GAIN

        # Get the ADC readings by doing the average of acquisitions
        total_voltage = 0
        total_current = 0
        for a in range(acquisitions):
            raw_channels = ads.read_sequence(resistance_channels)
            voltages = [i * ads.v_per_digit for i in raw_channels]
            print(voltages)
            total_voltage += raw_channels[0]
            total_current += raw_channels[1]

        mean_voltage = (total_voltage / acquisitions) * ads.v_per_digit
        mean_current = (total_current / acquisitions) * ads.v_per_digit

        # Calculate the resistance and the calibrated resistance
        # Uses the INA146 gain to find the real voltages before they be amplified
        resistor_voltage = mean_voltage/hw_gain[1]
        resistor_current = mean_current/hw_gain[0]
        resistance = float(resistor_voltage) / float(resistor_current)

        print("Tensão raw: ", resistor_voltage)
        print("Corrente raw: ", resistor_current)
        print("Resistencia raw: ", resistance)

        # Turn off the ohmmeters relay
        self.range_select(ESC_OFF)

        # Return the tuple with data
        return resistance

    def get_temperature(self):
        temperature_raw = ads.read_oneshot(TEMPERATURE_CHANNEL)
        temperature_voltage = temperature_raw * ads.v_per_digit
        temperature = 100*temperature_voltage
        return temperature
