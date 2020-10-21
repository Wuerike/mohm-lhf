from PySide2 import QtCore

class KEYBOARD(QtCore.QObject):

    def __init__(self, window):
        super(KEYBOARD, self).__init__()
        self.window = window
        self.last_sender = None
        
        # keyboard itself events
        self.window.keyboard_0.clicked.connect(self.keyboard_add)
        self.window.keyboard_1.clicked.connect(self.keyboard_add)
        self.window.keyboard_2.clicked.connect(self.keyboard_add)
        self.window.keyboard_3.clicked.connect(self.keyboard_add)
        self.window.keyboard_4.clicked.connect(self.keyboard_add)
        self.window.keyboard_5.clicked.connect(self.keyboard_add)
        self.window.keyboard_6.clicked.connect(self.keyboard_add)
        self.window.keyboard_7.clicked.connect(self.keyboard_add)
        self.window.keyboard_8.clicked.connect(self.keyboard_add)
        self.window.keyboard_9.clicked.connect(self.keyboard_add)
        self.window.keyboard_dot.clicked.connect(self.keyboard_add)
        self.window.keyboard_mili.clicked.connect(self.keyboard_add)
        self.window.keyboard_micro.clicked.connect(self.keyboard_add)
        self.window.keyboard_ohm.clicked.connect(self.keyboard_add)
        self.window.keyboard_del.clicked.connect(self.keyboard_del)
        self.window.keyboard_enter.clicked.connect(self.keyboard_enter)

        # in main who calls keyboard
        self.window.main_rmax_field.clicked.connect(self.keyboard_called)
        self.window.main_rmin_field.clicked.connect(self.keyboard_called)

        # in calib who calls keyboard
        self.window.calib_offset1_field.clicked.connect(self.keyboard_called)
        self.window.calib_offset2_field.clicked.connect(self.keyboard_called)
        self.window.calib_offset3_field.clicked.connect(self.keyboard_called)
        self.window.calib_offset4_field.clicked.connect(self.keyboard_called)
        self.window.calib_offset5_field.clicked.connect(self.keyboard_called)
        self.window.calib_offset6_field.clicked.connect(self.keyboard_called)
        self.window.calib_offset7_field.clicked.connect(self.keyboard_called)
        self.window.calib_offset8_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain1_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain2_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain3_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain4_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain5_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain6_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain7_field.clicked.connect(self.keyboard_called)
        self.window.calib_gain8_field.clicked.connect(self.keyboard_called)

        # in comunication who calls keyboard
        self.window.com_port_field.clicked.connect(self.keyboard_called)

        # in config who calls keyboard
        self.window.config_temp_ref_field.clicked.connect(self.keyboard_called)
        self.window.config_aquisitions_field.clicked.connect(self.keyboard_called)
        self.window.config_stabilization_field.clicked.connect(self.keyboard_called)


    def keyboard_called(self):
        self.last_sender = self.sender()
        self.window.keyboard_field.setPlainText(self.last_sender.text())
        self.window.keyboard.raise_()


    def keyboard_add(self):
        sender = self.sender()
        old_text = self.window.keyboard_field.toPlainText()

        if ('Ω' in old_text):
            return

        if(sender.text() == '.'):
            if ('.' in old_text):
                return        

        new_text = old_text + sender.text()
        self.window.keyboard_field.setPlainText(new_text)


    def keyboard_del(self):
        old_text = self.window.keyboard_field.toPlainText()       
        size = len(old_text)

        if (size<1):
            return
        elif (old_text[size-2] == 'm' or old_text[size-2] == 'u'):
            new_text = old_text[:size-2]
        else:
            new_text = old_text[:size-1]
        self.window.keyboard_field.setPlainText(new_text)


    def keyboard_enter(self):
        self.last_sender.setText(self.window.keyboard_field.toPlainText())
        self.window.keyboard.lower()
