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
        self.INPUT1 = conf.INPUT1
        self.INPUT2 = conf.INPUT2
        self.INPUT3 = conf.INPUT3
        self.INPUT4 = conf.INPUT4

        # GPIO Outputs configuration, used to scaled selection
        for pin in (conf.ESC1_PIN, conf.ESC2_PIN, conf.ESC3_PIN, conf.GAIN_PIN):
            if pin is not None:
                wp.pinMode(pin, wp.OUTPUT)
                wp.digitalWrite(pin, wp.LOW)

        # GPIO Outputs configuration, used to scaled selection
        for pin in (conf.INPUT1, conf.INPUT2, conf.INPUT3, conf.INPUT4):
            if pin is not None:
                wp.pinMode(pin, wp.INPUT)

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
            '5': DRATE_100,
        }

        ads.drate = rate_options.get(data_rate, DRATE_2_5)

    def get_analog_values(self, scale, data_rate, stabilization, acquisitions):
        # Config data acquisition rate
        self.set_data_rate(data_rate)

        # Select the ohmmeters measurement range
        self.range_select(scale)

        # Stabilization time
        time.sleep(stabilization)

        # select which gain should be used
        if scale == ESC_1:
            resistance_channels = RESISTANCE_CHANNELS_1000_VOLTAGE_GAIN
        else:
            resistance_channels = RESISTANCE_CHANNELS_20_VOLTAGE_GAIN

        # Get the ADC readings by doing the average of acquisitions
        total_voltage = 0
        total_current = 0
        for a in range(acquisitions):
            raw_channels = ads.read_sequence(resistance_channels)
            total_voltage += raw_channels[0]
            total_current += raw_channels[1]

        # Turn off the ohmmeters relay
        self.range_select(ESC_OFF)

        mean_voltage = (total_voltage / acquisitions) * ads.v_per_digit
        mean_current = (total_current / acquisitions) * ads.v_per_digit

        print("Tensão média ina carga: ", mean_voltage)
        print("Tensão média ina shunt: ", mean_current)

        return mean_voltage, mean_current

    # Auto scale routine
    def auto_scale_selection(self, data_rate, stabilization, acquisitions):
        print(" ---- Realizando seleção de escala automatica ----")
        scale = ESC_1
        while scale <= ESC_8:
            mean_voltage, mean_current = self.get_analog_values(scale, data_rate, stabilization, acquisitions)
            if (mean_voltage <= 4.9 and scale!=ESC_2) or (mean_voltage <= 1 and scale==ESC_2):
                print(" --- Escala selecionada: ", scale)
                return scale
            else:
                scale += 1
        return ESC_8

    # Resistance measurement routine
    def do_measurement(self, scale, data_rate, stabilization, acquisitions):

        if(scale == ESC_OFF):
            scale = self.auto_scale_selection('2', stabilization, 1)

        mean_voltage, mean_current = self.get_analog_values(scale, data_rate, stabilization, acquisitions)

        # Calculate the resistance and the calibrated resistance
        # Uses the INA146/145 gain to find the real voltages before they be amplified
        # Define the proper Ina146 hardware gain
        hw_gain = self.hw_gain_per_scale(scale)
        load_voltage = mean_voltage/hw_gain[1]
        load_current = mean_current/hw_gain[0]
        resistance = float(load_voltage) / float(load_current)

        print("Tensão no carga: ", load_voltage)
        print("Corrente no shunt: ", load_current)
        print("Resistencia raw: ", resistance)

        # Return the tuple with data
        return resistance, scale

    def get_temperature(self):
        temperature_raw = ads.read_oneshot(TEMPERATURE_CHANNEL)
        temperature_voltage = temperature_raw * ads.v_per_digit
        temperature = 100*temperature_voltage
        return temperature

    def is_start_button_pressed(self):
        if wp.digitalRead(self.INPUT1) == wp.HIGH:
            return True
        else:
            return False
