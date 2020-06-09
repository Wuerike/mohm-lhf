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
    
    @QtCore.Slot(str, int)
    def modbus_start(self, ip, port):
        queue = SimpleQueue()
        Process(target=server.run_callback_server, args=(ip, port, queue)).start()

        while True:
            device, value = queue.get()
            print("Registrador: %s -> Valor: %s" % (device, value))

            if (device[0:2]=="di"):
                pass
            if (device[0:2]=="co"):
                if (value[0] == 1):
                    self.measure.emit()
            if (device[0:2]=="ir"):
                pass
            if (device[0:2]=="hr"):
                pass 

class MODBUS(QtCore.QObject):
    workerInit = QtCore.Signal(str, int)

    """docstring for MODBUS"""
    def __init__(self, window, measurement):
        super(MODBUS, self).__init__()
        self.window = window
        self.measurement = measurement

        self.thread = QtCore.QThread(self)
        self.thread.start()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        # signals from worker
        self.worker.error.connect(self.on_error)
        self.worker.measure.connect(self.test123456)
        # signals to worker
        self.workerInit.connect(self.worker.modbus_start)

        self.ip = self.window.com_ip_field.text()
        self.port = int(self.window.com_port_field.text())
        self.workerInit.emit(self.ip, self.port)


    @QtCore.Slot(str)
    def on_error(self, error):
        print(error)


    @QtCore.Slot()
    def test123456(self):
        self.measurement.do_measurement()


    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()
        super(MainWindow, self).closeEvent(event)