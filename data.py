from PySide2 import QtCore
import socket
import shutil
import json
import os


class DATA_MANAGEMENT(QtCore.QObject):

    def __init__(self, window):
        super(DATA_MANAGEMENT, self).__init__()
        self.window = window

        # Events to save data
        self.window.main_test_button.clicked.connect(self.save_main)
        self.window.calib_back_button.clicked.connect(self.save_calib)
        self.window.com_back_button.clicked.connect(self.save_comunication)
        self.window.config_back_button.clicked.connect(self.save_config)

        self.check_files()
        self.init_data()

    def get_ip_address(self):
        ip_address = ''
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8",80))
            ip_address = s.getsockname()[0]
            s.close()
        except:
            ip_address = "NO NETWORK"
        return ip_address

    def check_files(self):
        main = os.path.isfile('/home/pi/mohm-lhf/data/main.json')
        calib = os.path.isfile('/home/pi/mohm-lhf/data/calib.json')
        config = os.path.isfile('/home/pi/mohm-lhf/data/config.json')
        communication = os.path.isfile('/home/pi/mohm-lhf/data/comunication.json')

        if main and calib and config and communication:
            #cria um backup dos arquivos existentes e retorna
            shutil.copyfile('/home/pi/mohm-lhf/data/main.json', '/home/pi/mohm-lhf/data/main.bak')
            shutil.copyfile('/home/pi/mohm-lhf/data/calib.json', '/home/pi/mohm-lhf/data/calib.bak')
            shutil.copyfile('/home/pi/mohm-lhf/data/config.json', '/home/pi/mohm-lhf/data/config.bak')
            shutil.copyfile('/home/pi/mohm-lhf/data/comunication.json', '/home/pi/mohm-lhf/data/comunication.bak')
            return
        else:
            #copia os arquivos de backup e retorna
            shutil.copyfile('/home/pi/mohm-lhf/data/main.bak', '/home/pi/mohm-lhf/data/main.json')
            shutil.copyfile('/home/pi/mohm-lhf/data/calib.bak', '/home/pi/mohm-lhf/data/calib.json')
            shutil.copyfile('/home/pi/mohm-lhf/data/config.bak', '/home/pi/mohm-lhf/data/config.json')
            shutil.copyfile('/home/pi/mohm-lhf/data/comunication.bak', '/home/pi/mohm-lhf/data/comunication.json')
            return

    def init_data(self):
        with open('/home/pi/mohm-lhf/data/main.json') as main_file:
            main_data = json.load(main_file)

            self.window.main_scale_select.setCurrentIndex(main_data['scale'])
            self.window.main_rmin_field.setText(main_data['min-limit'])
            self.window.main_rmax_field.setText(main_data['max-limit'])
            self.window.config_material_field.setCurrentIndex(main_data['material'])

        with open('/home/pi/mohm-lhf/data/calib.json') as calib_file:
            calib_data = json.load(calib_file)

            self.window.calib_offset1_field.setText(calib_data[1]['offset'])
            self.window.calib_offset2_field.setText(calib_data[2]['offset'])
            self.window.calib_offset3_field.setText(calib_data[3]['offset'])
            self.window.calib_offset4_field.setText(calib_data[4]['offset'])
            self.window.calib_offset5_field.setText(calib_data[5]['offset'])
            self.window.calib_offset6_field.setText(calib_data[6]['offset'])
            self.window.calib_offset7_field.setText(calib_data[7]['offset'])
            self.window.calib_offset8_field.setText(calib_data[8]['offset'])
            self.window.calib_offset_temp_field.setText(calib_data[9]['offset'])

            self.window.calib_gain1_field.setText(calib_data[1]['gain'])
            self.window.calib_gain2_field.setText(calib_data[2]['gain'])
            self.window.calib_gain3_field.setText(calib_data[3]['gain'])
            self.window.calib_gain4_field.setText(calib_data[4]['gain'])
            self.window.calib_gain5_field.setText(calib_data[5]['gain'])
            self.window.calib_gain6_field.setText(calib_data[6]['gain'])
            self.window.calib_gain7_field.setText(calib_data[7]['gain'])
            self.window.calib_gain8_field.setText(calib_data[8]['gain'])
            self.window.calib_gain_temp_field.setText(calib_data[9]['gain'])

        with open('/home/pi/mohm-lhf/data/config.json') as config_file:
            config_data = json.load(config_file)

            self.window.config_temp_ref_field.setText(config_data['temp-ref'])
            self.window.config_data_rate_field.setCurrentIndex(config_data['data-rate'])
            self.window.config_aquisitions_field.setText(config_data['aquisitions'])
            self.window.config_stabilization_field.setText(config_data['stabilization'])

        with open('/home/pi/mohm-lhf/data/comunication.json') as com_file:
            com_data = json.load(com_file)
            self.window.com_ip_field.setText(self.get_ip_address())
            self.window.com_port_field.setText(com_data['port'])      

    def save_main(self):
        main_data = {
            "scale": self.window.main_scale_select.currentIndex(),
            "max-limit": self.window.main_rmax_field.text(), 
            "min-limit": self.window.main_rmin_field.text(),
            "material": self.window.config_material_field.currentIndex()
        }

        with open('/home/pi/mohm-lhf/data/main.json', 'w') as main_file:
            json.dump(main_data, main_file)

    def save_calib(self):
        calib_data = [
            {
                "offset": 0, 
                "gain": 0
            }, 
            {
                "offset": self.window.calib_offset1_field.text(), 
                "gain": self.window.calib_gain1_field.text()
            }, 
            {
                "offset": self.window.calib_offset2_field.text(), 
                "gain": self.window.calib_gain2_field.text()
            }, 
            {
                "offset": self.window.calib_offset3_field.text(),  
                "gain": self.window.calib_gain3_field.text()
            }, 
            {
                "offset": self.window.calib_offset4_field.text(),  
                "gain": self.window.calib_gain4_field.text()
            }, 
            {
                "offset": self.window.calib_offset5_field.text(),  
                "gain": self.window.calib_gain5_field.text()
            }, 
            {
                "offset": self.window.calib_offset6_field.text(),  
                "gain": self.window.calib_gain6_field.text()
            }, 
            {
                "offset": self.window.calib_offset7_field.text(),  
                "gain": self.window.calib_gain7_field.text()
            }, 
            {
                "offset": self.window.calib_offset8_field.text(),  
                "gain": self.window.calib_gain8_field.text()
            },
            {
                "offset": self.window.calib_offset_temp_field.text(),
                "gain": self.window.calib_gain_temp_field.text()
            }
        ]

        with open('/home/pi/mohm-lhf/data/calib.json', 'w') as calib_file:
            json.dump(calib_data, calib_file)

    def save_config(self):
        config_data = {
            "temp-ref": self.window.config_temp_ref_field.text(),
            "data-rate": self.window.config_data_rate_field.currentIndex(), 
            "aquisitions": self.window.config_aquisitions_field.text(), 
            "stabilization": self.window.config_stabilization_field.text()
        }

        with open('/home/pi/mohm-lhf/data/config.json', 'w') as config_file:
            json.dump(config_data, config_file)

    def save_comunication(self):
        com_data = {
            "port":  self.window.com_port_field.text(), 
        }

        with open('/home/pi/mohm-lhf/data/comunication.json', 'w') as com_file:
            json.dump(com_data, com_file)
