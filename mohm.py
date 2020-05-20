import time
import json
import wiringpi as wp
import mohm_definitions
from mohm_definitions import *
from ADS1256_definitions import *
from pipyadc import ADS1256

ads = ADS1256()

DIF1, DIF2 = POS_AIN0|NEG_AIN1, POS_AIN2|NEG_AIN3
CH_SEQUENCE = (DIF1, DIF2)

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
        escala = int(escala)
        wp.digitalWrite(self.ESC1_PIN, (0x01 & escala))
        wp.digitalWrite(self.ESC2_PIN, (0x02 & escala))
        wp.digitalWrite(self.ESC3_PIN, (0x04 & escala))


    def ADS_Calib(self):
        # Gain and offset self-calibration
        ads.cal_self()
        
    
    def gain_per_scale(self, escala):
        ganhos_escala = {
        '0': (0,0),
        '1': (20,2),
        '2': (2,2),
        '3': (0.2,2),
        '4': (20,2),
        '5': (20,2),
        '6': (20,2),
        '7': (20,2),
        }
        return ganhos_escala.get(escala, (0,0))
    

    def read_calib(self, scale):
        with open('calib.json') as calib_file:
            per_scale_calib_data = json.load(calib_file)
            offset = per_scale_calib_data[int(scale)]['offset']
            gain = per_scale_calib_data[int(scale)]['gain']
            return(offset,gain)


    def write_calib(self, data):
        with open('calib.json', 'w') as calib_file:
            json.dump(data, calib_file)


    # Resistence measurement routine
    def do_measurement(self, scale):
                
        # Select the ohmmimeter measurement range 
        self.range_select(scale)

        # Define the proper Ina146 hardware gain
        ina_gain = self.gain_per_scale(scale)

        # Read the calibration values
        offset_gain = self.read_calib(scale)
        
        # Estabilization time 
        time.sleep(0.2)
        
        # Get ADC data
        raw_channels = ads.read_sequence(CH_SEQUENCE)

        # Calculate the resistance and the calibrated resistance
        # Uses the INA146 gain to find the real voltages before they be amplified
        resistance = float(raw_channels[1]/ina_gain[0]) / float(raw_channels[0]/ina_gain[1])

        resistance_calib = offset_gain[0] + offset_gain[1]*resistance
        
        # Turn off the ohmmimeter's relay
        self.range_select(ESC_OFF)
        
        # Return the tuple with data
        return resistance_calib

    



