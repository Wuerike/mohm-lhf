from __future__ import print_function	# For Py2/3 compatibility
import eel
from random import *

# Give folder containing web files
eel.init('interface')              


# Expose this function to Javascript
@eel.expose                         
def pythonPrint(x):
    print('%s' % x)


@eel.expose 
def solicita_resitencia(escala):
	print("Escala:", escala)
	value= random()
	value = (f'{value:.4f}Ω')
	print (value)
	eel.recebe_resistencia(value)


# Start
eel.start('index.html', cmdline_args=['--kiosk'], port=0)    