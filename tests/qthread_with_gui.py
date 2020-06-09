# -*- coding: utf-8 -*- --noconsole

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from gui_core import Ui_MainWindow

from keyboard import KEYBOARD
from data import DATA_MANAGEMENT
from measurement import MEASUREMENT
#from communication import MODBUS

from multiprocessing import Process, SimpleQueue
#import callback_server as server
from time import sleep



class Worker(QtCore.QObject):

    error = QtCore.Signal(str)
    
    @QtCore.Slot(str)
    def infiniteLoop(self, value):
        if value == "1":
            while True:
                sleep(5)
                print('contou 5')
        else:
            self.error.emit("Try other value")



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    objInit = QtCore.Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.thread = QtCore.QThread(self)
        self.thread.start()
        self.obj = Worker()
        self.obj.moveToThread(self.thread)
        self.obj.error.connect(self.on_error)
        self.objInit.connect(self.obj.infiniteLoop)
        
        self.objInit.emit("1")


    @QtCore.Slot(str)
    def on_error(self, error):
        print(error)

    def closeEvent(self, event):
        self.thread.quit()
        self.thread.wait()
        super(MainWindow, self).closeEvent(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    measurement = MEASUREMENT(window)
    keyboard = KEYBOARD(window)
    data = DATA_MANAGEMENT(window)

    sys.exit(app.exec_())