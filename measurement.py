from PySide2 import QtCore
from mohm import OHMIMETRO
import json
from random import *

mohm = OHMIMETRO()
mohm.ADS_Calib()

class MEASUREMENT(QtCore.QObject):
    def __init__(self, window):
        super(MEASUREMENT, self).__init__()
        self.window = window
    
        self.CEM_MICRO = 0.0001
        self.UM_MILI = 0.001
        self.DEZ_MILI = 0.01
        self.CEM_MILI = 0.1
        self.UM = 1
        self.DEZ = 10
        self.CEM = 100
        self.MIL = 1000
        self.DEZ_MIL = 10000

        self.window.main_test_button.clicked.connect(self.do_measurement)
        self.window.main_setup_button.clicked.connect(self.get_temperature)


    def apply_multiplier(self, value):
        size = len(value)

        if (value[size-1] == 'Ω'):
            value = value[0:size-1]
            size = len(value)

        if (value[size-1] == 'u'):
            value = float(value[0:size-1])/1000000;
            return (value)

        if (value[size-1] == 'm'):
            value = float(value[0:size-1])/1000;
            return (value)

        else:
            return float(value)


    def limit_check(self, resistance):

        rmin = self.apply_multiplier(self.window.main_rmin_field.text())
        rmax = self.apply_multiplier(self.window.main_rmax_field.text())

        if (rmin > resistance):
            self.window.main_rmin_field.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.window.main_rmax_field.setStyleSheet("background-color: rgb(255, 255, 255);")

        elif (resistance > rmax):
            self.window.main_rmin_field.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.window.main_rmax_field.setStyleSheet("background-color: rgb(255, 0, 0);")

        else:
            self.window.main_rmin_field.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.window.main_rmax_field.setStyleSheet("background-color: rgb(0, 255, 0);")


    def resistance_format(self, value):
        if (value < self.CEM_MICRO):
            value = value * 1000000
            return ("%.3fuΩ" % value)

        elif (value < self.UM_MILI):
            value = value * 1000000
            return ("%.2fuΩ" % value)
        
        elif (value < self.DEZ_MILI):
            value = value * 1000
            return ("%.4fmΩ" % value)
        
        elif (value < self.CEM_MILI):
            value = value * 1000
            return ("%.3fmΩ" % value)
        
        elif (value < self.UM):
            value = value * 1000
            return ("%.2fmΩ" % value)
        
        elif (value < self.DEZ):
            return ("%.4fΩ" % value)
        
        elif (value < self.CEM):
            return ("%.3fΩ" % value)
        
        elif (value < self.MIL):
            return ("%.2fΩ" % value)
        
        elif (value < self.DEZ_MIL):
            return ("%.1fΩ" % value)
        
        else:
            return ("%.0fΩ" % value)


    def read_calib_per_scale(self, scale):
        with open('data/calib.json') as calib_file:
            per_scale_calib_data = json.load(calib_file)
            offset = per_scale_calib_data[int(scale)]['offset']
            gain = per_scale_calib_data[int(scale)]['gain']
            return(offset,gain)


    def do_measurement(self):
        # Get test parameters
        scale = self.window.main_scale_select.currentIndex()
        data_rate = self.window.config_data_rate_field.currentIndex()
        stabilization = float(self.window.config_stabilization_field.text())
        aquisitions = int(self.window.config_aquisitions_field.text())

        resistance = mohm.do_measurement(scale, data_rate, stabilization, aquisitions)

        offset_gain = self.read_calib_per_scale(scale)
        resistance_calib = float(offset_gain[0]) + float(offset_gain[1])*resistance

        actual_temp = self.get_temperature()
        ref_temp = float(self.window.config_temp_ref_field.text())
        material_factor = self.get_material_factor()

        resistance_temp_adjusted = resistance_calib * ( 1 + material_factor * (ref_temp - actual_temp) )

        print(resistance_temp_adjusted)

        resisistance_text = self.resistance_format(resistance_temp_adjusted)
        self.window.main_resistance_field.setText(resisistance_text)

        self.limit_check(resistance_calib)

    def get_temperature(self):
        # faz medição da temperatura
        temperature = mohm.get_temperature()
        self.window.setup_actual_temp_field.setText("%.1f" % temperature)
        return float("%.1f" % temperature)

    def get_material_factor(self):
        material = self.window.config_material_field.currentIndex()

        # Cupper selected
        if (material == 1):
            return 0.0040
        # Aluminium selected
        elif (material == 2):
            return 0.0036
        # None selected
        else:
            return 0


