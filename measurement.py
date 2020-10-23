from PySide2 import QtCore
from mohm import OHMIMETRO
import json

from time import sleep

mohm = OHMIMETRO()
mohm.ads_calib()


class Worker(QtCore.QObject):
    measure = QtCore.Signal()

    def __init__(self):
        super(Worker, self).__init__()

    @QtCore.Slot()
    def start_button_check(self):

        while True:
            if mohm.is_start_button_pressed():
                while mohm.is_start_button_pressed():
                    sleep(0.05)
                self.measure.emit()
            sleep(0.1)


class MEASUREMENT(QtCore.QObject):
    workerInit = QtCore.Signal()

    def __init__(self, window):
        super(MEASUREMENT, self).__init__()
        self.window = window

        # Constants definitions
        self.CEM_MICRO = 0.0001
        self.UM_MILI = 0.001
        self.DEZ_MILI = 0.01
        self.CEM_MILI = 0.1
        self.UM = 1
        self.DEZ = 10
        self.CEM = 100
        self.MIL = 1000
        self.DEZ_MIL = 10000

        # New thread criation to the worker class
        self.thread = QtCore.QThread(self)
        self.thread.start()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        # from worker signal connection
        self.worker.measure.connect(self.do_measurement)
        # to worker signal connection
        self.workerInit.connect(self.worker.start_button_check)

        # GUI buttons signals connection
        self.window.main_test_button.clicked.connect(self.do_measurement)
        self.window.main_setup_button.clicked.connect(self.get_temperature)

        # Emit worker init signal
        self.workerInit.emit()

    def apply_multiplier(self, value):
        size = len(value)

        if value[size - 1] == 'Ω':
            value = value[0:size - 1]
            size = len(value)

        if value[size - 1] == 'u':
            value = float(value[0:size - 1]) / 1000000;
            return (value)

        if value[size - 1] == 'm':
            value = float(value[0:size - 1]) / 1000;
            return (value)

        else:
            return float(value)

    def limit_check(self, resistance):
        rmin = self.apply_multiplier(self.window.main_rmin_field.text())
        rmax = self.apply_multiplier(self.window.main_rmax_field.text())

        if rmin > resistance:
            self.window.main_rmin_field.setStyleSheet(
                u"background-color: rgb(255, 0, 0); color: rgb(0, 0, 0); border: none; border-radius: 15px;")
            self.window.main_rmax_field.setStyleSheet(
                u"background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border: none; border-radius: 15px;")

        elif resistance > rmax:
            self.window.main_rmin_field.setStyleSheet(
                u"background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border: none; border-radius: 15px;")
            self.window.main_rmax_field.setStyleSheet(
                u"background-color: rgb(255, 0, 0); color: rgb(0, 0, 0); border: none; border-radius: 15px;")

        else:
            self.window.main_rmin_field.setStyleSheet(
                u"background-color: rgb(0, 255, 0); color: rgb(0, 0, 0); border: none; border-radius: 15px;")
            self.window.main_rmax_field.setStyleSheet(
                u"background-color: rgb(0, 255, 0); color: rgb(0, 0, 0); border: none; border-radius: 15px;")

    def resistance_format(self, value):
        if value < self.CEM_MICRO:
            value = value * 1000000
            return "%.3fuΩ" % value

        elif value < self.UM_MILI:
            value = value * 1000000
            return "%.2fuΩ" % value

        elif value < self.DEZ_MILI:
            value = value * 1000
            return "%.4fmΩ" % value

        elif value < self.CEM_MILI:
            value = value * 1000
            return "%.3fmΩ" % value

        elif value < self.UM:
            value = value * 1000
            return "%.2fmΩ" % value

        elif value < self.DEZ:
            return "%.4fΩ" % value

        elif value < self.CEM:
            return "%.3fΩ" % value

        elif value < self.MIL:
            return "%.2fΩ" % value

        elif value < self.DEZ_MIL:
            return "%.1fΩ" % value

        else:
            return "%.0fΩ" % value

    def read_calib_per_scale(self, scale):
        with open('/home/pi/mohm-lhf/data/calib.json') as calib_file:
            per_scale_calib_data = json.load(calib_file)
            offset = per_scale_calib_data[int(scale)]['offset']
            gain = per_scale_calib_data[int(scale)]['gain']
            return offset, gain

    def do_measurement(self):
        # Get test parameters
        scale = self.window.main_scale_select.currentIndex()
        data_rate = self.window.config_data_rate_field.currentIndex()
        stabilization = float(self.window.config_stabilization_field.text())
        acquisitions = int(self.window.config_aquisitions_field.text())

        print("#####################")
        print("Escala: ", scale, "Taxa: ", data_rate, "Estabilização: ", stabilization, "Aquisições: ", acquisitions)

        resistance, scale = mohm.do_measurement(scale, data_rate, stabilization, acquisitions)
        offset_gain = self.read_calib_per_scale(scale)
        resistance_calib = float(offset_gain[0]) + float(offset_gain[1]) * resistance
        actual_temp = self.get_temperature()
        ref_temp = float(self.window.config_temp_ref_field.text())
        material_factor = self.get_material_factor()
        resistance_temp_adjusted = resistance_calib * (1 + material_factor * (ref_temp - actual_temp))

        print("Resistencia calibrada: ", resistance_temp_adjusted)

        resistance_text = self.resistance_format(resistance_temp_adjusted)
        self.window.main_resistance_field.setText(resistance_text)
        self.add_to_measurement_table(resistance_text)
        self.limit_check(resistance_temp_adjusted)

    def add_to_measurement_table(self, last_resistance):
        third_last_resistance = self.window.main_2nd_last_res_field.text()
        second_last_resistance = self.window.main_last_res_field.text()
        self.window.main_3rd_last_res_field.setText(third_last_resistance)
        self.window.main_2nd_last_res_field.setText(second_last_resistance)
        self.window.main_last_res_field.setText(last_resistance)            

        resistance_list = []
        total_resistance = 0
        for resistance in (last_resistance, second_last_resistance, third_last_resistance):
            if(resistance != ''):
                resistance = self.apply_multiplier(resistance)
                total_resistance += resistance
                resistance_list.append(resistance)

        mean_resistance = total_resistance/len(resistance_list)

        percentage_error = []
        for resistance in resistance_list:
            error = abs(1 - mean_resistance/resistance)*100
            percentage_error.append(error)

        max_error = ("%.3f" % max(percentage_error)) 
        print(max_error)
        self.window.main_last_res_error_field.setText(max_error+"%")

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
