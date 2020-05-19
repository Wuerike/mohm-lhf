from __future__ import print_function	# For Py2/3 compatibility
import eel
from mohm import OHMIMETRO
from random import *

mohm = OHMIMETRO()

# Give folder containing web files
eel.init('interface')              

# Expose this function to Javascript
@eel.expose                         
def pythonPrint(x):
    print('%s' % x)


@eel.expose 
def solicita_resitencia(escala):
	eel.recebe_resistencia(mohm.do_measurement(escala))


if __name__ == '__main__':
	mohm.ADS_Calib()
	eel.start('index.html', cmdline_args=['--kiosk'], port=0)    