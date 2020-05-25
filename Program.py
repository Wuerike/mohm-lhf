# -*- coding: utf-8 -*- --noconsole

import sys
from PySide2 import QtCore, QtGui, QtWidgets
from gui_core import Ui_MainWindow

#from mohm import OHMIMETRO
import json
from random import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

def main(window):
	#mohm = OHMIMETRO()

	def do_measurement():
		scale = window.scale_select.currentIndex()
		#resistance = mohm.do_measurement(scale)
		#offset_gain = read_calib_per_scale(scale)
		#resistance_calib = offset_gain[0] + offset_gain[1]*resistance
		#print(resistance_calib)
		resistance = random()
		window.resistance_field.setPlainText( "{:0.4f}".format(resistance+scale) )

	window.test_button.clicked.connect(do_measurement)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    main(window)
    sys.exit(app.exec_())