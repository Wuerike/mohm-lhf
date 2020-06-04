import time
import json
import wiringpi as wp
import mohm_definitions
from mohm_definitions import *
from ADS1256_definitions import *
from pipyadc import ADS1256

ads = ADS1256()

RESISTENCE_CHANNELS = (POS_AIN0|NEG_AIN1, POS_AIN2|NEG_AIN3)
TEMPERATURE_CHANNEL = (POS_AIN4|NEG_AIN5)

class OHMIMETRO(object):
    

    def __init__(self, conf=mohm_definitions):
        # Set up the wiringpi object to use physical pin numbers
        wp.wiringPiSetupPhys()
        # Config and initialize the SPI and GPIO pins used by the ADC.
        # The following four entries are actively used by the code:
        self.ESC1_PIN   = conf.ESC1_PIN
        self.ESC2_PIN   = conf.ESC2_PIN
        self.ESC3_PIN   = conf.ESC3_PIN

        # GPIO Outputs. Only the CS_PIN is currently actively used. ~RESET and 
        # ~PDWN must be set to static logic HIGH level if not hardwired:
        for pin in (conf.ESC1_PIN,
                    conf.ESC2_PIN,
                    conf.ESC3_PIN):
            if pin is not None:
                wp.pinMode(pin, wp.OUTPUT)
                wp.digitalWrite(pin, wp.LOW)        

    def range_select(self, escala):
        wp.digitalWrite(self.ESC1_PIN, (0x01 & escala))
        wp.digitalWrite(self.ESC2_PIN, (0x02 & escala))
        wp.digitalWrite(self.ESC3_PIN, (0x04 & escala))


    def ADS_Calib(self):
        # Gain and offset self-calibration
        ads.cal_self()


    # compensates the each shunt and the INA's fixed gain
    def hw_gain_per_scale(self, escala):
        escala = str(escala)
        ganhos_escala = {
        '0': (0,0),
        '1': (2,20),
        '2': (20,20),
        '3': (200,20),
        '4': (20,20),
        '5': (20,20),
        '6': (20,20),
        '7': (20,20),
        }
        return ganhos_escala.get(escala, (0,0))


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


    # Resistence measurement routine
    def do_measurement(self, scale, data_rate, stabilization, aquisitions):
        
        # Config data aquisition rate
        self.set_data_rate(data_rate)

        # Select the ohmmimeter measurement range 
        self.range_select(scale)

        # Define the proper Ina146 hardware gain
        hw_gain = self.hw_gain_per_scale(scale)
        
        # Estabilization time 
        time.sleep(stabilization)
        
        # Get ADC data
        total_voltage = 0
        total_current = 0
        for a in range(aquisitions):
            raw_channels = ads.read_sequence(RESISTENCE_CHANNELS)
            total_voltage += raw_channels[1]
            total_current += raw_channels[0]

        mean_voltage = total_voltage / aquisitions
        mean_current = total_current / aquisitions
        
        # Calculate the resistance and the calibrated resistance
        # Uses the INA146 gain to find the real voltages before they be amplified
        resistance = float(mean_voltage/hw_gain[1]) / float(mean_current/hw_gain[0])

        #resistance_calib = offset_gain[0] + offset_gain[1]*resistance

        # Turn off the ohmmimeter's relay
        self.range_select(ESC_OFF)

        # Return the tuple with data
        return resistance


    def get_temperature(self):
        temperature_raw = ads.read_oneshot(TEMPERATURE_CHANNEL)
        temperature_voltage = temperature_raw * ads.v_per_digit
        temperature = 100*temperature_voltage
        return temperature



