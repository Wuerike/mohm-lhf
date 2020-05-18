from __future__ import print_function	# For Py2/3 compatibility
import eel
#from random import *

 # Give folder containing web files
eel.init('interface')              

# Start
eel.start('index.html', cmdline_args=['--kiosk'])    
