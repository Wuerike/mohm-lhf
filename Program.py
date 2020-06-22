# -*- coding: utf-8 -*- --noconsole

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from gui_core import Ui_MainWindow

from measurement import MEASUREMENT
from keyboard import KEYBOARD
from data import DATA_MANAGEMENT
from communication import MODBUS

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showFullScreen()

    measurement = MEASUREMENT(window)
    keyboard = KEYBOARD(window)
    data = DATA_MANAGEMENT(window)
    communication = MODBUS(window, measurement)

    sys.exit(app.exec_())