from __future__ import print_function	# For Py2/3 compatibility
import eel
#from mohm import OHMIMETRO
from random import *
import json

#mohm = OHMIMETRO()

# Give folder containing web files
eel.init('interface')              

# Expose this function to Javascript
@eel.expose                         
def pythonPrint(x):
    print('%s' % x)


@eel.expose
def save_calib_data(calib_data):
	#mohm.write_calib(calib_data)
	with open('calib.json', 'w') as calib_file:
		json.dump(calib_data, calib_file)

@eel.expose
def read_calib():
	with open('calib.json') as calib_file:
		per_scale_calib_data = json.load(calib_file)
		print(per_scale_calib_data)
		eel.update_calib_data(per_scale_calib_data)

@eel.expose 
def solicita_resitencia(escala):
	eel.recebe_resistencia(mohm.do_measurement(escala))


if __name__ == '__main__':
	#mohm.ADS_Calib()
	eel.start('calib.html', cmdline_args=['--kiosk'], port=0)    