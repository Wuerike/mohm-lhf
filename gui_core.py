# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_core.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1920, 1080))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        icon = QIcon()
        icon.addFile(u"Y:/Marketing LHF/Manual de Marca LHF - FINAL/logo pequena_amplificador.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.main = QFrame(self.frame)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, 0, 1920, 1080))
        self.main.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.verticalLayoutWidget_3 = QWidget(self.main)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(570, 120, 1252, 841))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.main_scale_select = QComboBox(self.verticalLayoutWidget_3)
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.setObjectName(u"main_scale_select")
        self.main_scale_select.setMinimumSize(QSize(1250, 150))
        font = QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.main_scale_select.setFont(font)
        self.main_scale_select.setFocusPolicy(Qt.NoFocus)
        self.main_scale_select.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.main_scale_select.setMaxVisibleItems(8)
        self.main_scale_select.setFrame(False)

        self.verticalLayout_9.addWidget(self.main_scale_select)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_18)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_2 = QLabel(self.verticalLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(250, 150))
        self.label_2.setMaximumSize(QSize(250, 150))
        font1 = QFont()
        font1.setPointSize(50)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_19, 1, 1, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(250, 150))
        self.label.setMaximumSize(QSize(250, 150))
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.main_rmax_field = QPushButton(self.verticalLayoutWidget_3)
        self.main_rmax_field.setObjectName(u"main_rmax_field")
        self.main_rmax_field.setEnabled(True)
        self.main_rmax_field.setMinimumSize(QSize(400, 150))
        self.main_rmax_field.setMaximumSize(QSize(16777215, 150))
        font2 = QFont()
        font2.setPointSize(80)
        font2.setBold(True)
        font2.setWeight(75)
        self.main_rmax_field.setFont(font2)
        self.main_rmax_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.main_rmax_field, 0, 1, 1, 1)

        self.main_rmin_field = QPushButton(self.verticalLayoutWidget_3)
        self.main_rmin_field.setObjectName(u"main_rmin_field")
        self.main_rmin_field.setEnabled(True)
        self.main_rmin_field.setMinimumSize(QSize(400, 150))
        self.main_rmin_field.setMaximumSize(QSize(16777215, 150))
        self.main_rmin_field.setFont(font2)
        self.main_rmin_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.main_rmin_field, 2, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_6)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_20)

        self.main_resistance_field = QPushButton(self.verticalLayoutWidget_3)
        self.main_resistance_field.setObjectName(u"main_resistance_field")
        self.main_resistance_field.setEnabled(False)
        self.main_resistance_field.setMinimumSize(QSize(400, 200))
        self.main_resistance_field.setMaximumSize(QSize(16777215, 200))
        font3 = QFont()
        font3.setPointSize(150)
        font3.setBold(True)
        font3.setWeight(75)
        self.main_resistance_field.setFont(font3)
        self.main_resistance_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.main_resistance_field)

        self.verticalLayoutWidget_4 = QWidget(self.main)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(100, 120, 429, 841))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.main_setup_button = QPushButton(self.verticalLayoutWidget_4)
        self.main_setup_button.setObjectName(u"main_setup_button")
        self.main_setup_button.setEnabled(True)
        self.main_setup_button.setMinimumSize(QSize(400, 200))
        self.main_setup_button.setMaximumSize(QSize(16777215, 200))
        self.main_setup_button.setFont(font2)
        self.main_setup_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.main_setup_button)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_16)

        self.main_menu_button = QPushButton(self.verticalLayoutWidget_4)
        self.main_menu_button.setObjectName(u"main_menu_button")
        self.main_menu_button.setEnabled(True)
        self.main_menu_button.setMinimumSize(QSize(0, 200))
        self.main_menu_button.setMaximumSize(QSize(16777215, 200))
        self.main_menu_button.setFont(font2)
        self.main_menu_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.main_menu_button)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_17)

        self.main_test_button = QPushButton(self.verticalLayoutWidget_4)
        self.main_test_button.setObjectName(u"main_test_button")
        self.main_test_button.setEnabled(True)
        self.main_test_button.setMinimumSize(QSize(0, 200))
        self.main_test_button.setMaximumSize(QSize(16777215, 200))
        font4 = QFont()
        font4.setPointSize(75)
        font4.setBold(True)
        font4.setWeight(75)
        self.main_test_button.setFont(font4)
        self.main_test_button.setStyleSheet(u"background-color: rgb(143, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.main_test_button)

        self.setup = QFrame(self.frame)
        self.setup.setObjectName(u"setup")
        self.setup.setGeometry(QRect(0, 0, 1920, 1080))
        self.setup.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.setup_frame = QFrame(self.setup)
        self.setup_frame.setObjectName(u"setup_frame")
        self.setup_frame.setGeometry(QRect(100, 100, 1720, 880))
        self.setup_frame.setFrameShape(QFrame.StyledPanel)
        self.setup_frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.setup_frame)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(-1, -1, 1721, 881))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.setup_back_button = QPushButton(self.gridLayoutWidget_4)
        self.setup_back_button.setObjectName(u"setup_back_button")
        self.setup_back_button.setEnabled(True)
        self.setup_back_button.setMinimumSize(QSize(300, 100))
        self.setup_back_button.setMaximumSize(QSize(300, 100))
        font5 = QFont()
        font5.setPointSize(30)
        font5.setBold(True)
        font5.setWeight(75)
        self.setup_back_button.setFont(font5)
        self.setup_back_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_5.addWidget(self.setup_back_button, 7, 1, 1, 1, Qt.AlignRight)

        self.setup_temp_ref_field = QPushButton(self.gridLayoutWidget_4)
        self.setup_temp_ref_field.setObjectName(u"setup_temp_ref_field")
        self.setup_temp_ref_field.setEnabled(False)
        self.setup_temp_ref_field.setMinimumSize(QSize(300, 100))
        self.setup_temp_ref_field.setMaximumSize(QSize(300, 100))
        self.setup_temp_ref_field.setFont(font1)
        self.setup_temp_ref_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.setup_temp_ref_field, 1, 1, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(1200, 100))
        self.label_24.setMaximumSize(QSize(1200, 100))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_24.setIndent(10)

        self.gridLayout_5.addWidget(self.label_24, 5, 0, 1, 1)

        self.setup_actual_temp_field = QPushButton(self.gridLayoutWidget_4)
        self.setup_actual_temp_field.setObjectName(u"setup_actual_temp_field")
        self.setup_actual_temp_field.setEnabled(False)
        self.setup_actual_temp_field.setMinimumSize(QSize(300, 100))
        self.setup_actual_temp_field.setMaximumSize(QSize(300, 100))
        self.setup_actual_temp_field.setFont(font1)
        self.setup_actual_temp_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.setup_actual_temp_field, 0, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QSize(1200, 100))
        self.label_23.setMaximumSize(QSize(1200, 100))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_23.setIndent(10)

        self.gridLayout_5.addWidget(self.label_23, 6, 0, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_4)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(1200, 100))
        self.label_27.setMaximumSize(QSize(1200, 100))
        font6 = QFont()
        font6.setPointSize(47)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_27.setFont(font6)
        self.label_27.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_27.setIndent(10)

        self.gridLayout_5.addWidget(self.label_27, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.setup_stabilization_field = QPushButton(self.gridLayoutWidget_4)
        self.setup_stabilization_field.setObjectName(u"setup_stabilization_field")
        self.setup_stabilization_field.setEnabled(False)
        self.setup_stabilization_field.setMinimumSize(QSize(300, 100))
        self.setup_stabilization_field.setMaximumSize(QSize(300, 100))
        self.setup_stabilization_field.setFont(font1)
        self.setup_stabilization_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.setup_stabilization_field)


        self.gridLayout_5.addLayout(self.horizontalLayout_6, 6, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.setup_aquisitions_field = QPushButton(self.gridLayoutWidget_4)
        self.setup_aquisitions_field.setObjectName(u"setup_aquisitions_field")
        self.setup_aquisitions_field.setEnabled(False)
        self.setup_aquisitions_field.setMinimumSize(QSize(300, 100))
        self.setup_aquisitions_field.setMaximumSize(QSize(300, 100))
        self.setup_aquisitions_field.setFont(font1)
        self.setup_aquisitions_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_8.addWidget(self.setup_aquisitions_field)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 5, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.setup_material_field = QComboBox(self.gridLayoutWidget_4)
        self.setup_material_field.addItem("")
        self.setup_material_field.addItem("")
        self.setup_material_field.addItem("")
        self.setup_material_field.setObjectName(u"setup_material_field")
        self.setup_material_field.setEnabled(False)
        self.setup_material_field.setMinimumSize(QSize(300, 100))
        self.setup_material_field.setMaximumSize(QSize(300, 100))
        font7 = QFont()
        font7.setPointSize(40)
        font7.setBold(True)
        font7.setWeight(75)
        self.setup_material_field.setFont(font7)
        self.setup_material_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.setup_material_field)


        self.gridLayout_5.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(1200, 100))
        self.label_26.setMaximumSize(QSize(1200, 100))
        self.label_26.setFont(font1)
        self.label_26.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_26.setIndent(10)

        self.gridLayout_5.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(1200, 100))
        self.label_25.setMaximumSize(QSize(1200, 100))
        self.label_25.setFont(font1)
        self.label_25.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_25.setIndent(10)

        self.gridLayout_5.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_29 = QLabel(self.gridLayoutWidget_4)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QSize(1200, 100))
        self.label_29.setMaximumSize(QSize(1200, 100))
        self.label_29.setFont(font1)
        self.label_29.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_29.setIndent(10)

        self.gridLayout_5.addWidget(self.label_29, 3, 0, 1, 1)

        self.setup_data_rate_field = QComboBox(self.gridLayoutWidget_4)
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.setObjectName(u"setup_data_rate_field")
        self.setup_data_rate_field.setEnabled(False)
        self.setup_data_rate_field.setMinimumSize(QSize(300, 100))
        self.setup_data_rate_field.setMaximumSize(QSize(300, 100))
        font8 = QFont()
        font8.setPointSize(45)
        font8.setBold(True)
        font8.setWeight(75)
        self.setup_data_rate_field.setFont(font8)
        self.setup_data_rate_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_5.addWidget(self.setup_data_rate_field, 3, 1, 1, 1)

        self.menu = QFrame(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 1920, 1080))
        self.menu.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.gridLayoutWidget = QWidget(self.menu)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(400, 200, 1121, 681))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.menu_calib_button = QPushButton(self.gridLayoutWidget)
        self.menu_calib_button.setObjectName(u"menu_calib_button")
        self.menu_calib_button.setEnabled(True)
        self.menu_calib_button.setMinimumSize(QSize(0, 200))
        self.menu_calib_button.setMaximumSize(QSize(16777215, 200))
        self.menu_calib_button.setFont(font5)
        self.menu_calib_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.menu_calib_button, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.menu_config_button = QPushButton(self.gridLayoutWidget)
        self.menu_config_button.setObjectName(u"menu_config_button")
        self.menu_config_button.setEnabled(True)
        self.menu_config_button.setMinimumSize(QSize(400, 200))
        self.menu_config_button.setMaximumSize(QSize(400, 200))
        self.menu_config_button.setFont(font5)
        self.menu_config_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.menu_config_button, 0, 0, 1, 1)

        self.menu_back_button = QPushButton(self.gridLayoutWidget)
        self.menu_back_button.setObjectName(u"menu_back_button")
        self.menu_back_button.setEnabled(True)
        self.menu_back_button.setMinimumSize(QSize(0, 200))
        self.menu_back_button.setMaximumSize(QSize(16777215, 200))
        self.menu_back_button.setFont(font5)
        self.menu_back_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.menu_back_button, 2, 2, 1, 1)

        self.menu_com_button = QPushButton(self.gridLayoutWidget)
        self.menu_com_button.setObjectName(u"menu_com_button")
        self.menu_com_button.setEnabled(True)
        self.menu_com_button.setMinimumSize(QSize(400, 200))
        self.menu_com_button.setMaximumSize(QSize(400, 200))
        self.menu_com_button.setFont(font5)
        self.menu_com_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.menu_com_button, 0, 2, 1, 1)

        self.config = QFrame(self.frame)
        self.config.setObjectName(u"config")
        self.config.setGeometry(QRect(0, 0, 1920, 1080))
        self.config.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.config_frame = QFrame(self.config)
        self.config_frame.setObjectName(u"config_frame")
        self.config_frame.setGeometry(QRect(100, 100, 1720, 880))
        self.config_frame.setFrameShape(QFrame.StyledPanel)
        self.config_frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.config_frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(-1, -1, 1721, 881))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.gridLayoutWidget_3)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(1200, 100))
        self.label_22.setMaximumSize(QSize(1200, 100))
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_22.setIndent(10)

        self.gridLayout_4.addWidget(self.label_22, 4, 0, 1, 1)

        self.config_back_button = QPushButton(self.gridLayoutWidget_3)
        self.config_back_button.setObjectName(u"config_back_button")
        self.config_back_button.setEnabled(True)
        self.config_back_button.setMinimumSize(QSize(300, 100))
        self.config_back_button.setMaximumSize(QSize(300, 100))
        self.config_back_button.setFont(font5)
        self.config_back_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.config_back_button, 5, 1, 1, 1, Qt.AlignRight)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.config_stabilization_field = QPushButton(self.gridLayoutWidget_3)
        self.config_stabilization_field.setObjectName(u"config_stabilization_field")
        self.config_stabilization_field.setEnabled(True)
        self.config_stabilization_field.setMinimumSize(QSize(300, 100))
        self.config_stabilization_field.setMaximumSize(QSize(300, 100))
        self.config_stabilization_field.setFont(font1)
        self.config_stabilization_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.config_stabilization_field)


        self.gridLayout_4.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.config_material_field = QComboBox(self.gridLayoutWidget_3)
        self.config_material_field.addItem("")
        self.config_material_field.addItem("")
        self.config_material_field.addItem("")
        self.config_material_field.setObjectName(u"config_material_field")
        self.config_material_field.setMinimumSize(QSize(300, 100))
        self.config_material_field.setMaximumSize(QSize(300, 100))
        self.config_material_field.setFont(font7)
        self.config_material_field.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.config_material_field)


        self.gridLayout_4.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.config_temp_ref_field = QPushButton(self.gridLayoutWidget_3)
        self.config_temp_ref_field.setObjectName(u"config_temp_ref_field")
        self.config_temp_ref_field.setEnabled(True)
        self.config_temp_ref_field.setMinimumSize(QSize(300, 100))
        self.config_temp_ref_field.setMaximumSize(QSize(300, 100))
        self.config_temp_ref_field.setFont(font1)
        self.config_temp_ref_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_4.addWidget(self.config_temp_ref_field, 0, 1, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget_3)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(1200, 100))
        self.label_21.setMaximumSize(QSize(1200, 100))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_21.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_21.setIndent(10)

        self.gridLayout_4.addWidget(self.label_21, 3, 0, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_3)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(1200, 100))
        self.label_19.setMaximumSize(QSize(1200, 100))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_19.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_19.setIndent(10)

        self.gridLayout_4.addWidget(self.label_19, 0, 0, 1, 1)

        self.config_save_button = QPushButton(self.gridLayoutWidget_3)
        self.config_save_button.setObjectName(u"config_save_button")
        self.config_save_button.setEnabled(True)
        self.config_save_button.setMinimumSize(QSize(300, 100))
        self.config_save_button.setMaximumSize(QSize(300, 100))
        self.config_save_button.setFont(font5)
        self.config_save_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.config_save_button, 5, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.config_aquisitions_field = QPushButton(self.gridLayoutWidget_3)
        self.config_aquisitions_field.setObjectName(u"config_aquisitions_field")
        self.config_aquisitions_field.setEnabled(True)
        self.config_aquisitions_field.setMinimumSize(QSize(300, 100))
        self.config_aquisitions_field.setMaximumSize(QSize(300, 100))
        self.config_aquisitions_field.setFont(font1)
        self.config_aquisitions_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.config_aquisitions_field)


        self.gridLayout_4.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_3)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(1200, 100))
        self.label_20.setMaximumSize(QSize(1200, 100))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_20.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_20.setIndent(10)

        self.gridLayout_4.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_3)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(1200, 100))
        self.label_28.setMaximumSize(QSize(1200, 100))
        self.label_28.setFont(font1)
        self.label_28.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_28.setIndent(10)

        self.gridLayout_4.addWidget(self.label_28, 2, 0, 1, 1)

        self.config_data_rate_field = QComboBox(self.gridLayoutWidget_3)
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.setObjectName(u"config_data_rate_field")
        self.config_data_rate_field.setMinimumSize(QSize(300, 100))
        self.config_data_rate_field.setMaximumSize(QSize(300, 100))
        self.config_data_rate_field.setFont(font8)
        self.config_data_rate_field.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.config_data_rate_field, 2, 1, 1, 1)

        self.calib = QFrame(self.frame)
        self.calib.setObjectName(u"calib")
        self.calib.setGeometry(QRect(0, 0, 1920, 1080))
        self.calib.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.gridLayoutWidget_2 = QWidget(self.calib)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(140, 10, 1691, 1072))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.calib_back_button = QPushButton(self.gridLayoutWidget_2)
        self.calib_back_button.setObjectName(u"calib_back_button")
        self.calib_back_button.setEnabled(True)
        self.calib_back_button.setMinimumSize(QSize(300, 100))
        self.calib_back_button.setMaximumSize(QSize(300, 100))
        self.calib_back_button.setFont(font5)
        self.calib_back_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.calib_back_button, 8, 2, 1, 1, Qt.AlignRight)

        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(0, 100))
        self.label_17.setMaximumSize(QSize(300, 100))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setIndent(0)

        self.gridLayout_3.addWidget(self.label_17, 6, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(300, 100))
        self.label_12.setMaximumSize(QSize(300, 100))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setIndent(0)

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(500, 100))
        self.label_11.setMaximumSize(QSize(500, 100))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_11, 0, 2, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(0, 100))
        self.label_18.setMaximumSize(QSize(300, 100))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setIndent(0)

        self.gridLayout_3.addWidget(self.label_18, 7, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(0, 100))
        self.label_16.setMaximumSize(QSize(300, 100))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setIndent(0)

        self.gridLayout_3.addWidget(self.label_16, 4, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(500, 100))
        self.label_10.setMaximumSize(QSize(500, 100))
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_10, 0, 1, 1, 1)

        self.calib_save_button = QPushButton(self.gridLayoutWidget_2)
        self.calib_save_button.setObjectName(u"calib_save_button")
        self.calib_save_button.setEnabled(True)
        self.calib_save_button.setMinimumSize(QSize(300, 100))
        self.calib_save_button.setMaximumSize(QSize(300, 100))
        self.calib_save_button.setFont(font5)
        self.calib_save_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.calib_save_button, 8, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(0, 100))
        self.label_14.setMaximumSize(QSize(300, 100))
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setIndent(0)

        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(0, 100))
        self.label_15.setMaximumSize(QSize(300, 100))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setIndent(0)

        self.gridLayout_3.addWidget(self.label_15, 5, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(0, 100))
        self.label_13.setMaximumSize(QSize(300, 100))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setIndent(0)

        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(300, 100))
        self.label_9.setMaximumSize(QSize(300, 100))
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 1)

        self.calib_offset1_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_offset1_field.setObjectName(u"calib_offset1_field")
        self.calib_offset1_field.setEnabled(True)
        self.calib_offset1_field.setMinimumSize(QSize(500, 100))
        self.calib_offset1_field.setMaximumSize(QSize(500, 100))
        self.calib_offset1_field.setFont(font2)
        self.calib_offset1_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_offset1_field, 1, 1, 1, 1)

        self.calib_offset2_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_offset2_field.setObjectName(u"calib_offset2_field")
        self.calib_offset2_field.setEnabled(True)
        self.calib_offset2_field.setMinimumSize(QSize(500, 100))
        self.calib_offset2_field.setMaximumSize(QSize(500, 100))
        self.calib_offset2_field.setFont(font2)
        self.calib_offset2_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_offset2_field, 2, 1, 1, 1)

        self.calib_offset3_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_offset3_field.setObjectName(u"calib_offset3_field")
        self.calib_offset3_field.setEnabled(True)
        self.calib_offset3_field.setMinimumSize(QSize(500, 100))
        self.calib_offset3_field.setMaximumSize(QSize(500, 100))
        self.calib_offset3_field.setFont(font2)
        self.calib_offset3_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_offset3_field, 3, 1, 1, 1)

        self.calib_offset4_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_offset4_field.setObjectName(u"calib_offset4_field")
        self.calib_offset4_field.setEnabled(True)
        self.calib_offset4_field.setMinimumSize(QSize(500, 100))
        self.calib_offset4_field.setMaximumSize(QSize(500, 100))
        self.calib_offset4_field.setFont(font2)
        self.calib_offset4_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_offset4_field, 4, 1, 1, 1)

        self.calib_offset5_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_offset5_field.setObjectName(u"calib_offset5_field")
        self.calib_offset5_field.setEnabled(True)
        self.calib_offset5_field.setMinimumSize(QSize(500, 100))
        self.calib_offset5_field.setMaximumSize(QSize(500, 100))
        self.calib_offset5_field.setFont(font2)
        self.calib_offset5_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_offset5_field, 5, 1, 1, 1)

        self.calib_offset6_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_offset6_field.setObjectName(u"calib_offset6_field")
        self.calib_offset6_field.setEnabled(True)
        self.calib_offset6_field.setMinimumSize(QSize(500, 100))
        self.calib_offset6_field.setMaximumSize(QSize(500, 100))
        self.calib_offset6_field.setFont(font2)
        self.calib_offset6_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_offset6_field, 6, 1, 1, 1)

        self.calib_offset7_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_offset7_field.setObjectName(u"calib_offset7_field")
        self.calib_offset7_field.setEnabled(True)
        self.calib_offset7_field.setMinimumSize(QSize(500, 100))
        self.calib_offset7_field.setMaximumSize(QSize(500, 100))
        self.calib_offset7_field.setFont(font2)
        self.calib_offset7_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_offset7_field, 7, 1, 1, 1)

        self.calib_gain1_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_gain1_field.setObjectName(u"calib_gain1_field")
        self.calib_gain1_field.setEnabled(True)
        self.calib_gain1_field.setMinimumSize(QSize(500, 100))
        self.calib_gain1_field.setMaximumSize(QSize(500, 100))
        self.calib_gain1_field.setFont(font2)
        self.calib_gain1_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_gain1_field, 1, 2, 1, 1)

        self.calib_gain2_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_gain2_field.setObjectName(u"calib_gain2_field")
        self.calib_gain2_field.setEnabled(True)
        self.calib_gain2_field.setMinimumSize(QSize(500, 100))
        self.calib_gain2_field.setMaximumSize(QSize(500, 100))
        self.calib_gain2_field.setFont(font2)
        self.calib_gain2_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_gain2_field, 2, 2, 1, 1)

        self.calib_gain3_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_gain3_field.setObjectName(u"calib_gain3_field")
        self.calib_gain3_field.setEnabled(True)
        self.calib_gain3_field.setMinimumSize(QSize(500, 100))
        self.calib_gain3_field.setMaximumSize(QSize(500, 100))
        self.calib_gain3_field.setFont(font2)
        self.calib_gain3_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_gain3_field, 3, 2, 1, 1)

        self.calib_gain4_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_gain4_field.setObjectName(u"calib_gain4_field")
        self.calib_gain4_field.setEnabled(True)
        self.calib_gain4_field.setMinimumSize(QSize(500, 100))
        self.calib_gain4_field.setMaximumSize(QSize(500, 100))
        self.calib_gain4_field.setFont(font2)
        self.calib_gain4_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_gain4_field, 4, 2, 1, 1)

        self.calib_gain5_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_gain5_field.setObjectName(u"calib_gain5_field")
        self.calib_gain5_field.setEnabled(True)
        self.calib_gain5_field.setMinimumSize(QSize(500, 100))
        self.calib_gain5_field.setMaximumSize(QSize(500, 100))
        self.calib_gain5_field.setFont(font2)
        self.calib_gain5_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_gain5_field, 5, 2, 1, 1)

        self.calib_gain6_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_gain6_field.setObjectName(u"calib_gain6_field")
        self.calib_gain6_field.setEnabled(True)
        self.calib_gain6_field.setMinimumSize(QSize(500, 100))
        self.calib_gain6_field.setMaximumSize(QSize(500, 100))
        self.calib_gain6_field.setFont(font2)
        self.calib_gain6_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_gain6_field, 6, 2, 1, 1)

        self.calib_gain7_field = QPushButton(self.gridLayoutWidget_2)
        self.calib_gain7_field.setObjectName(u"calib_gain7_field")
        self.calib_gain7_field.setEnabled(True)
        self.calib_gain7_field.setMinimumSize(QSize(500, 100))
        self.calib_gain7_field.setMaximumSize(QSize(500, 100))
        self.calib_gain7_field.setFont(font2)
        self.calib_gain7_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.calib_gain7_field, 7, 2, 1, 1)

        self.comunication = QFrame(self.frame)
        self.comunication.setObjectName(u"comunication")
        self.comunication.setGeometry(QRect(0, 0, 1920, 1080))
        self.comunication.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.verticalLayoutWidget_5 = QWidget(self.comunication)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(250, 170, 1424, 741))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_8 = QLabel(self.verticalLayoutWidget_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(250, 150))
        self.label_8.setMaximumSize(QSize(250, 150))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.label_8.setIndent(-1)

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_7 = QLabel(self.verticalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(250, 150))
        self.label_7.setMaximumSize(QSize(250, 150))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setIndent(-1)

        self.gridLayout_7.addWidget(self.label_7, 1, 0, 1, 1)

        self.com_ip_field = QPushButton(self.verticalLayoutWidget_5)
        self.com_ip_field.setObjectName(u"com_ip_field")
        self.com_ip_field.setEnabled(True)
        self.com_ip_field.setMinimumSize(QSize(0, 150))
        self.com_ip_field.setMaximumSize(QSize(16777215, 150))
        self.com_ip_field.setFont(font2)
        self.com_ip_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_7.addWidget(self.com_ip_field, 0, 1, 1, 1)

        self.com_port_field = QPushButton(self.verticalLayoutWidget_5)
        self.com_port_field.setObjectName(u"com_port_field")
        self.com_port_field.setEnabled(True)
        self.com_port_field.setMinimumSize(QSize(0, 150))
        self.com_port_field.setMaximumSize(QSize(16777215, 150))
        self.com_port_field.setFont(font2)
        self.com_port_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_7.addWidget(self.com_port_field, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.com_init_button = QPushButton(self.verticalLayoutWidget_5)
        self.com_init_button.setObjectName(u"com_init_button")
        self.com_init_button.setEnabled(True)
        self.com_init_button.setMinimumSize(QSize(350, 200))
        self.com_init_button.setMaximumSize(QSize(350, 200))
        self.com_init_button.setFont(font5)
        self.com_init_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.com_init_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.com_close_button = QPushButton(self.verticalLayoutWidget_5)
        self.com_close_button.setObjectName(u"com_close_button")
        self.com_close_button.setEnabled(True)
        self.com_close_button.setMinimumSize(QSize(350, 200))
        self.com_close_button.setMaximumSize(QSize(350, 200))
        self.com_close_button.setFont(font5)
        self.com_close_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.com_close_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.com_back_button = QPushButton(self.verticalLayoutWidget_5)
        self.com_back_button.setObjectName(u"com_back_button")
        self.com_back_button.setEnabled(True)
        self.com_back_button.setMinimumSize(QSize(350, 200))
        self.com_back_button.setMaximumSize(QSize(350, 200))
        self.com_back_button.setFont(font5)
        self.com_back_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.com_back_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.keyboard = QFrame(self.frame)
        self.keyboard.setObjectName(u"keyboard")
        self.keyboard.setGeometry(QRect(0, 0, 1920, 1080))
        self.keyboard.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.keyboard.setFrameShape(QFrame.StyledPanel)
        self.keyboard.setFrameShadow(QFrame.Raised)
        self.keyboard_frame = QFrame(self.keyboard)
        self.keyboard_frame.setObjectName(u"keyboard_frame")
        self.keyboard_frame.setGeometry(QRect(250, 100, 1421, 880))
        self.keyboard_frame.setStyleSheet(u"")
        self.keyboard_frame.setFrameShape(QFrame.StyledPanel)
        self.keyboard_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.keyboard_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1422, 879))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.keyboard_field = QPlainTextEdit(self.verticalLayoutWidget)
        self.keyboard_field.setObjectName(u"keyboard_field")
        self.keyboard_field.setMaximumSize(QSize(16777215, 150))
        font9 = QFont()
        font9.setPointSize(80)
        self.keyboard_field.setFont(font9)
        self.keyboard_field.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.keyboard_field)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.keyboard_8 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_8.setObjectName(u"keyboard_8")
        self.keyboard_8.setEnabled(True)
        self.keyboard_8.setMinimumSize(QSize(350, 150))
        self.keyboard_8.setMaximumSize(QSize(350, 150))
        self.keyboard_8.setFont(font2)
        self.keyboard_8.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_8, 0, 1, 1, 1)

        self.keyboard_9 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_9.setObjectName(u"keyboard_9")
        self.keyboard_9.setEnabled(True)
        self.keyboard_9.setMinimumSize(QSize(350, 150))
        self.keyboard_9.setMaximumSize(QSize(350, 150))
        self.keyboard_9.setFont(font2)
        self.keyboard_9.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_9, 0, 2, 1, 1)

        self.keyboard_1 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_1.setObjectName(u"keyboard_1")
        self.keyboard_1.setEnabled(True)
        self.keyboard_1.setMinimumSize(QSize(350, 150))
        self.keyboard_1.setMaximumSize(QSize(350, 150))
        self.keyboard_1.setFont(font2)
        self.keyboard_1.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_1, 2, 0, 1, 1)

        self.keyboard_7 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_7.setObjectName(u"keyboard_7")
        self.keyboard_7.setEnabled(True)
        self.keyboard_7.setMinimumSize(QSize(350, 150))
        self.keyboard_7.setMaximumSize(QSize(350, 150))
        self.keyboard_7.setFont(font2)
        self.keyboard_7.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_7, 0, 0, 1, 1)

        self.keyboard_4 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_4.setObjectName(u"keyboard_4")
        self.keyboard_4.setEnabled(True)
        self.keyboard_4.setMinimumSize(QSize(350, 150))
        self.keyboard_4.setMaximumSize(QSize(350, 150))
        self.keyboard_4.setFont(font2)
        self.keyboard_4.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_4, 1, 0, 1, 1)

        self.keyboard_micro = QPushButton(self.verticalLayoutWidget)
        self.keyboard_micro.setObjectName(u"keyboard_micro")
        self.keyboard_micro.setEnabled(True)
        self.keyboard_micro.setMinimumSize(QSize(350, 150))
        self.keyboard_micro.setMaximumSize(QSize(350, 150))
        self.keyboard_micro.setFont(font2)
        self.keyboard_micro.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_micro, 0, 3, 1, 1)

        self.keyboard_0 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_0.setObjectName(u"keyboard_0")
        self.keyboard_0.setEnabled(True)
        self.keyboard_0.setMinimumSize(QSize(350, 150))
        self.keyboard_0.setMaximumSize(QSize(350, 150))
        self.keyboard_0.setFont(font2)
        self.keyboard_0.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_0, 3, 0, 1, 1)

        self.keyboard_5 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_5.setObjectName(u"keyboard_5")
        self.keyboard_5.setEnabled(True)
        self.keyboard_5.setMinimumSize(QSize(350, 150))
        self.keyboard_5.setMaximumSize(QSize(350, 150))
        self.keyboard_5.setFont(font2)
        self.keyboard_5.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_5, 1, 1, 1, 1)

        self.keyboard_2 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_2.setObjectName(u"keyboard_2")
        self.keyboard_2.setEnabled(True)
        self.keyboard_2.setMinimumSize(QSize(350, 150))
        self.keyboard_2.setMaximumSize(QSize(350, 150))
        self.keyboard_2.setFont(font2)
        self.keyboard_2.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_2, 2, 1, 1, 1)

        self.keyboard_dot = QPushButton(self.verticalLayoutWidget)
        self.keyboard_dot.setObjectName(u"keyboard_dot")
        self.keyboard_dot.setEnabled(True)
        self.keyboard_dot.setMinimumSize(QSize(350, 150))
        self.keyboard_dot.setMaximumSize(QSize(350, 150))
        self.keyboard_dot.setFont(font2)
        self.keyboard_dot.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_dot, 3, 1, 1, 1)

        self.keyboard_6 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_6.setObjectName(u"keyboard_6")
        self.keyboard_6.setEnabled(True)
        self.keyboard_6.setMinimumSize(QSize(350, 150))
        self.keyboard_6.setMaximumSize(QSize(350, 150))
        self.keyboard_6.setFont(font2)
        self.keyboard_6.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_6, 1, 2, 1, 1)

        self.keyboard_3 = QPushButton(self.verticalLayoutWidget)
        self.keyboard_3.setObjectName(u"keyboard_3")
        self.keyboard_3.setEnabled(True)
        self.keyboard_3.setMinimumSize(QSize(350, 150))
        self.keyboard_3.setMaximumSize(QSize(350, 150))
        self.keyboard_3.setFont(font2)
        self.keyboard_3.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_3, 2, 2, 1, 1)

        self.keyboard_mili = QPushButton(self.verticalLayoutWidget)
        self.keyboard_mili.setObjectName(u"keyboard_mili")
        self.keyboard_mili.setEnabled(True)
        self.keyboard_mili.setMinimumSize(QSize(350, 150))
        self.keyboard_mili.setMaximumSize(QSize(350, 150))
        self.keyboard_mili.setFont(font2)
        self.keyboard_mili.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_mili, 1, 3, 1, 1)

        self.keyboard_ohm = QPushButton(self.verticalLayoutWidget)
        self.keyboard_ohm.setObjectName(u"keyboard_ohm")
        self.keyboard_ohm.setEnabled(True)
        self.keyboard_ohm.setMinimumSize(QSize(350, 150))
        self.keyboard_ohm.setMaximumSize(QSize(350, 150))
        self.keyboard_ohm.setFont(font2)
        self.keyboard_ohm.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_ohm, 2, 3, 1, 1)

        self.keyboard_enter = QPushButton(self.verticalLayoutWidget)
        self.keyboard_enter.setObjectName(u"keyboard_enter")
        self.keyboard_enter.setEnabled(True)
        self.keyboard_enter.setMinimumSize(QSize(350, 150))
        self.keyboard_enter.setMaximumSize(QSize(350, 150))
        font10 = QFont()
        font10.setPointSize(60)
        font10.setBold(True)
        font10.setWeight(75)
        self.keyboard_enter.setFont(font10)
        self.keyboard_enter.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_enter, 3, 3, 1, 1)

        self.keyboard_del = QPushButton(self.verticalLayoutWidget)
        self.keyboard_del.setObjectName(u"keyboard_del")
        self.keyboard_del.setEnabled(True)
        self.keyboard_del.setMinimumSize(QSize(350, 150))
        self.keyboard_del.setMaximumSize(QSize(350, 150))
        self.keyboard_del.setFont(font10)
        self.keyboard_del.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout_9.addWidget(self.keyboard_del, 3, 2, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_9)

        self.menu.raise_()
        self.keyboard.raise_()
        self.calib.raise_()
        self.comunication.raise_()
        self.config.raise_()
        self.setup.raise_()
        self.main.raise_()

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.com_back_button.clicked.connect(self.menu.raise_)
        self.calib_back_button.clicked.connect(self.menu.raise_)
        self.menu_com_button.clicked.connect(self.comunication.raise_)
        self.menu_calib_button.clicked.connect(self.calib.raise_)
        self.menu_config_button.clicked.connect(self.config.raise_)
        self.config_back_button.clicked.connect(self.menu.raise_)
        self.main_setup_button.clicked.connect(self.setup.raise_)
        self.setup_back_button.clicked.connect(self.main.raise_)
        self.main_menu_button.clicked.connect(self.menu.raise_)
        self.menu_back_button.clicked.connect(self.main.raise_)

        self.main_scale_select.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Miliohmimetro", None))
        self.main_scale_select.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE UMA ESCALA", None))
        self.main_scale_select.setItemText(1, QCoreApplication.translate("MainWindow", u"ESCALA 1 - RANGE: 20u\u03a9 - 200u\u03a9", None))
        self.main_scale_select.setItemText(2, QCoreApplication.translate("MainWindow", u"ESCALA 2 - RANGE: 200u\u03a9 - 2m\u03a9", None))
        self.main_scale_select.setItemText(3, QCoreApplication.translate("MainWindow", u"ESCALA 3 - RANGE: 2m\u03a9 - 20m\u03a9", None))
        self.main_scale_select.setItemText(4, QCoreApplication.translate("MainWindow", u"ESCALA 4 - RANGE: 20m\u03a9 - 200m\u03a9", None))
        self.main_scale_select.setItemText(5, QCoreApplication.translate("MainWindow", u"ESCALA 5 - RANGE: 200m\u03a9 - 2\u03a9", None))
        self.main_scale_select.setItemText(6, QCoreApplication.translate("MainWindow", u"ESCALA 6 - RANGE: 2\u03a9 - 20\u03a9", None))
        self.main_scale_select.setItemText(7, QCoreApplication.translate("MainWindow", u"ESCALA 7 - RANGE: > 20\u03a9", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rmin", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rm\u00e1x", None))
        self.main_rmax_field.setText("")
        self.main_rmin_field.setText("")
        self.main_resistance_field.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.main_setup_button.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.main_menu_button.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.main_test_button.setText(QCoreApplication.translate("MainWindow", u"TESTAR", None))
        self.setup_back_button.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.setup_temp_ref_field.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO DE AQUISI\u00c7\u00d5ES", None))
        self.setup_actual_temp_field.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"TEMPO DE ESTABILIZA\u00c7\u00c3O", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURA AMBIENTE ATUAL", None))
        self.setup_stabilization_field.setText("")
        self.setup_aquisitions_field.setText("")
        self.setup_material_field.setItemText(0, QCoreApplication.translate("MainWindow", u"NENHUM", None))
        self.setup_material_field.setItemText(1, QCoreApplication.translate("MainWindow", u"COBRE", None))
        self.setup_material_field.setItemText(2, QCoreApplication.translate("MainWindow", u"ALUM\u00cdNIO", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"METERIAL EM TESTE", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURA DE REFER\u00caNCIA", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"VELOCIDADE DE AQUISI\u00c7\u00c3O", None))
        self.setup_data_rate_field.setItemText(0, QCoreApplication.translate("MainWindow", u"2.5 SPS", None))
        self.setup_data_rate_field.setItemText(1, QCoreApplication.translate("MainWindow", u"5 SPS", None))
        self.setup_data_rate_field.setItemText(2, QCoreApplication.translate("MainWindow", u"10 SPS", None))
        self.setup_data_rate_field.setItemText(3, QCoreApplication.translate("MainWindow", u"15 SPS", None))
        self.setup_data_rate_field.setItemText(4, QCoreApplication.translate("MainWindow", u"25 SPS", None))

        self.menu_calib_button.setText(QCoreApplication.translate("MainWindow", u"CALIBRA\u00c7\u00c3O", None))
        self.menu_config_button.setText(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00c3O", None))
        self.menu_back_button.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.menu_com_button.setText(QCoreApplication.translate("MainWindow", u"COMUNICA\u00c7\u00c3O", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"TEMPO DE ESTABILIZA\u00c7\u00c3O", None))
        self.config_back_button.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.config_stabilization_field.setText("")
        self.config_material_field.setItemText(0, QCoreApplication.translate("MainWindow", u"NENHUM", None))
        self.config_material_field.setItemText(1, QCoreApplication.translate("MainWindow", u"COBRE", None))
        self.config_material_field.setItemText(2, QCoreApplication.translate("MainWindow", u"ALUM\u00cdNIO", None))

        self.config_temp_ref_field.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO DE AQUISI\u00c7\u00d5ES", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURA DE REFER\u00caNCIA", None))
        self.config_save_button.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.config_aquisitions_field.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"METERIAL EM TESTE", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"VELOCIDADE DE AQUISI\u00c7\u00c3O", None))
        self.config_data_rate_field.setItemText(0, QCoreApplication.translate("MainWindow", u"2.5 SPS", None))
        self.config_data_rate_field.setItemText(1, QCoreApplication.translate("MainWindow", u"5 SPS", None))
        self.config_data_rate_field.setItemText(2, QCoreApplication.translate("MainWindow", u"10 SPS", None))
        self.config_data_rate_field.setItemText(3, QCoreApplication.translate("MainWindow", u"15 SPS", None))
        self.config_data_rate_field.setItemText(4, QCoreApplication.translate("MainWindow", u"25 SPS", None))

        self.calib_back_button.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"GANHO", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"OFFSET", None))
        self.calib_save_button.setText(QCoreApplication.translate("MainWindow", u"SALVAR", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ESCALA", None))
        self.calib_offset1_field.setText("")
        self.calib_offset2_field.setText("")
        self.calib_offset3_field.setText("")
        self.calib_offset4_field.setText("")
        self.calib_offset5_field.setText("")
        self.calib_offset6_field.setText("")
        self.calib_offset7_field.setText("")
        self.calib_gain1_field.setText("")
        self.calib_gain2_field.setText("")
        self.calib_gain3_field.setText("")
        self.calib_gain4_field.setText("")
        self.calib_gain5_field.setText("")
        self.calib_gain6_field.setText("")
        self.calib_gain7_field.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PORTA", None))
        self.com_ip_field.setText("")
        self.com_port_field.setText("")
        self.com_init_button.setText(QCoreApplication.translate("MainWindow", u"INICIAR", None))
        self.com_close_button.setText(QCoreApplication.translate("MainWindow", u"FECHAR", None))
        self.com_back_button.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.keyboard_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.keyboard_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.keyboard_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.keyboard_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.keyboard_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.keyboard_micro.setText(QCoreApplication.translate("MainWindow", u"u\u03a9", None))
        self.keyboard_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.keyboard_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.keyboard_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.keyboard_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.keyboard_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.keyboard_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.keyboard_mili.setText(QCoreApplication.translate("MainWindow", u"m\u03a9", None))
        self.keyboard_ohm.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.keyboard_enter.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
        self.keyboard_del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
    # retranslateUi

