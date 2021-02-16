# -*- coding: utf-8 -*- --noconsole

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from gui_core import Ui_MainWindow

from multiprocessing import Process, SimpleQueue
import modbus_server as server
from time import sleep


class Worker(QtCore.QObject):
    error = QtCore.Signal(str)
    measure = QtCore.Signal()
    holdReg = QtCore.Signal(str, int)
    inputReg = QtCore.Signal(str)

    def __init__(self):
        super(Worker, self).__init__()
        self.inputRegData = None


    @QtCore.Slot(str, int)
    def modbus_start(self, ip, port):
        queue_receive = SimpleQueue()
        queue_send = SimpleQueue()
        Process(target=server.run_callback_server, args=(ip, port, queue_receive, queue_send)).start()

        while True:
            device, value = queue_receive.get()
            print("Registrador: %s -> Valor: %s" % (device, value))
            print(device, value)
            regType = device[0:2]
            regNum = device[2]
            
            # Bool enviados para o cliente (python -> labview)
            if (regType == "di"):
                queue_send.put([1, 0, 0, 1, 1, 0, 0, 1])

            # Bool recebidos do cliente (labview -> python)
            if (regType == "co"):
                if (value[0] == 1):
                    self.measure.emit()

            # Int enviados para o cliente (python -> labview)
            if (regType == "ir"):
                self.inputReg.emit(regNum)
                # tempo para garantir que a variavel vai ser atualizada
                sleep(0.1) 
                queue_send.put([self.inputRegData])
                
            # Int recebido do cliente (labview -> python)
            if (regType == "hr"):
                self.holdReg.emit(regNum, value[0])


    def setInputReg(self, value):
        self.inputRegData = value

class MODBUS(QtCore.QObject):
    workerInit = QtCore.Signal(str, int)

    """docstring for MODBUS"""
    def __init__(self, window, measurement):
        super(MODBUS, self).__init__()
        self.window = window
        self.measurement = measurement
        self.multiplier = 0
        self.temperature = 0

        self.thread = QtCore.QThread(self)
        self.thread.start()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        # signals from worker
        self.worker.error.connect(self.on_error)
        self.worker.measure.connect(self.do_measurement)
        self.worker.holdReg.connect(self.setHoldReg)
        self.worker.inputReg.connect(self.getInputReg)
        # signals to worker
        self.workerInit.connect(self.worker.modbus_start)

        self.ip = self.window.com_ip_field.text()
        self.port = int(self.window.com_port_field.text())
        self.workerInit.emit(self.ip, self.port)


    @QtCore.Slot(str)
    def on_error(self, error):
        print(error)


    @QtCore.Slot()
    def do_measurement(self):
        self.measurement.do_measurement()
        self.temperature = int(10*self.measurement.get_temperature())


    @QtCore.Slot(str, int)
    def setHoldReg(self, regNum, value):
        print(f'regNum = {regNum} e value = {value}')
        if (regNum == '0'):
            value = 0 if ((value<0) or (value>5)) else value
            self.window.main_scale_select.setCurrentIndex(value)

        elif (regNum == '1'):
            value = 20 if ((value<15) or (value>25)) else value
            self.window.config_temp_ref_field.setText(str(value))

        elif (regNum == '2'):
            value = 0 if ((value<0) or (value>2)) else value
            self.window.config_material_field.setCurrentIndex(value)

        elif (regNum == '3'):
            value = 1 if ((value<1) or (value>50)) else value
            self.window.config_aquisitions_field.setText(str(value))

        elif (regNum == '4'):
            value = 500 if ((value<1) or (value>10000)) else value
            self.window.config_stabilization_field.setText(str(value/1000))

        elif (regNum == '5'):
            pass
        elif (regNum == '6'):
            pass
        elif (regNum == '7'):
            pass

    @QtCore.Slot(str)
    def getInputReg(self, regNum):
        if (regNum == '0'):
            value = self.measurement.apply_multiplier(self.window.main_resistance_field.text())
            if (value < 0.01):
                value = int(value * 1000000)
                self.multiplier = 6
            elif (value < 0.1):
                value = int(value * 100000)
                self.multiplier = 5
            elif (value < 1):
                value = int(value * 10000)
                self.multiplier = 4
            elif (value < 10):
                value = int(value * 1000)
                self.multiplier = 3
            elif (value < 100):
                value = int(value * 100)
                self.multiplier = 2

        elif (regNum == '1'):
            value = self.multiplier

        elif (regNum == '2'):
            value = self.window.main_scale_select.currentIndex()

        elif (regNum == '3'):
            value = int(self.window.config_temp_ref_field.text())

        elif (regNum == '4'):
            value = self.window.config_material_field.currentIndex()

        elif (regNum == '5'):
            value = int(self.window.config_aquisitions_field.text())

        elif (regNum == '6'):
            value = int(float(self.window.config_stabilization_field.text())*1000)

        elif (regNum == '7'):
            value = self.temperature

        self.worker.setInputReg(value)


    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()
        super(MainWindow, self).closeEvent(event)
