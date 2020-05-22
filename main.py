from multiprocessing import SimpleQueue, Process
from mohm import OHMIMETRO
import eel
import json

mohm = OHMIMETRO()

# Give folder containing web files
eel.init('interface')              

def gui_start():
	eel.start('index.html', cmdline_args=['--kiosk'], port=0)

# Functions exposed to Javascript
@eel.expose                         
def pythonPrint(x):
    print('%s' % x)


@eel.expose
def save_index_init(index_data):
	with open('index_data.json', 'w') as index_file:
		json.dump(index_data, index_file)


@eel.expose
def read_index_init():
	with open('index_data.json') as index_file:
		index_data = json.load(index_file)
		eel.index_init(index_data)


@eel.expose
def save_calib_data(calib_data):
	with open('calib.json', 'w') as calib_file:
		json.dump(calib_data, calib_file)


def read_calib_per_scale(scale):
	with open('calib.json') as calib_file:
		per_scale_calib_data = json.load(calib_file)
		offset = per_scale_calib_data[int(scale)]['offset']
		gain = per_scale_calib_data[int(scale)]['gain']
		return(offset,gain)


@eel.expose
def read_calib():
	with open('calib.json') as calib_file:
		all_scale_calib_data = json.load(calib_file)
		eel.update_calib_data(all_scale_calib_data)


@eel.expose 
def solicita_resitencia(scale):
	resistance = mohm.do_measurement(scale)
	offset_gain = read_calib_per_scale(scale)
	resistance_calib = offset_gain[0] + offset_gain[1]*resistance
	print(resistance_calib)
	eel.recebe_resistencia(resistance_calib)


if __name__ == '__main__':
	mohm.ADS_Calib()
	Process(target=gui_start, args=()).start() 