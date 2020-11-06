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

import src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 593)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame {\n"
"   background-color: rgb(0, 0, 0);\n"
"   border: none;\n"
"};\n"
"\n"
"QPushButton{\n"
"   border: none;\n"
"}")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet(u"border-color: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.calib = QFrame(self.frame)
        self.calib.setObjectName(u"calib")
        self.calib.setGeometry(QRect(0, 0, 1024, 600))
        self.calib.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg_larger.png);\n"
"};")
        self.calib.setFrameShape(QFrame.StyledPanel)
        self.calib.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.calib)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(106, 20, 811, 551))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_14)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 811, 551))
        self.gridLayoutWidget_5.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(20)
        self.gridLayoutWidget_5.setFont(font)
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.gridLayoutWidget_5)
        self.label_33.setObjectName(u"label_33")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QSize(0, 60))
        self.label_33.setMaximumSize(QSize(150, 60))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_33.setFont(font1)
        self.label_33.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_33, 6, 0, 1, 1)

        self.calib_offset3_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset3_field.setObjectName(u"calib_offset3_field")
        self.calib_offset3_field.setEnabled(True)
        self.calib_offset3_field.setMinimumSize(QSize(300, 60))
        self.calib_offset3_field.setMaximumSize(QSize(300, 60))
        self.calib_offset3_field.setFont(font1)
        self.calib_offset3_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset3_field, 4, 1, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_5)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(0, 60))
        self.label_31.setMaximumSize(QSize(150, 60))
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_31, 4, 0, 1, 1)

        self.calib_gain1_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain1_field.setObjectName(u"calib_gain1_field")
        self.calib_gain1_field.setEnabled(True)
        self.calib_gain1_field.setMinimumSize(QSize(300, 60))
        self.calib_gain1_field.setMaximumSize(QSize(300, 60))
        self.calib_gain1_field.setFont(font1)
        self.calib_gain1_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain1_field, 2, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(0, 60))
        self.label_16.setMaximumSize(QSize(150, 60))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(0, 60))
        self.label_18.setMaximumSize(QSize(150, 60))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_18, 0, 0, 1, 1)

        self.calib_next_button = QPushButton(self.gridLayoutWidget_5)
        self.calib_next_button.setObjectName(u"calib_next_button")
        self.calib_next_button.setEnabled(True)
        self.calib_next_button.setMinimumSize(QSize(200, 75))
        self.calib_next_button.setMaximumSize(QSize(200, 75))
        self.calib_next_button.setFont(font1)
        self.calib_next_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.calib_next_button.setIconSize(QSize(25, 25))

        self.gridLayout_6.addWidget(self.calib_next_button, 9, 2, 1, 1, Qt.AlignRight)

        self.label_17 = QLabel(self.gridLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(0, 60))
        self.label_17.setMaximumSize(QSize(150, 60))
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_17, 3, 0, 1, 1)

        self.calib_gain3_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain3_field.setObjectName(u"calib_gain3_field")
        self.calib_gain3_field.setEnabled(True)
        self.calib_gain3_field.setMinimumSize(QSize(300, 60))
        self.calib_gain3_field.setMaximumSize(QSize(300, 60))
        self.calib_gain3_field.setFont(font1)
        self.calib_gain3_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain3_field, 4, 2, 1, 1)

        self.calib_offset2_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset2_field.setObjectName(u"calib_offset2_field")
        self.calib_offset2_field.setEnabled(True)
        self.calib_offset2_field.setMinimumSize(QSize(300, 60))
        self.calib_offset2_field.setMaximumSize(QSize(300, 60))
        self.calib_offset2_field.setFont(font1)
        self.calib_offset2_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset2_field, 3, 1, 1, 1)

        self.calib_gain4_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain4_field.setObjectName(u"calib_gain4_field")
        self.calib_gain4_field.setEnabled(True)
        self.calib_gain4_field.setMinimumSize(QSize(300, 60))
        self.calib_gain4_field.setMaximumSize(QSize(300, 60))
        self.calib_gain4_field.setFont(font1)
        self.calib_gain4_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain4_field, 5, 2, 1, 1)

        self.calib_gain2_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain2_field.setObjectName(u"calib_gain2_field")
        self.calib_gain2_field.setEnabled(True)
        self.calib_gain2_field.setMinimumSize(QSize(300, 60))
        self.calib_gain2_field.setMaximumSize(QSize(300, 60))
        self.calib_gain2_field.setFont(font1)
        self.calib_gain2_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain2_field, 3, 2, 1, 1)

        self.calib_offset4_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset4_field.setObjectName(u"calib_offset4_field")
        self.calib_offset4_field.setEnabled(True)
        self.calib_offset4_field.setMinimumSize(QSize(300, 60))
        self.calib_offset4_field.setMaximumSize(QSize(300, 60))
        self.calib_offset4_field.setFont(font1)
        self.calib_offset4_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset4_field, 5, 1, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(0, 60))
        self.label_19.setMaximumSize(QSize(300, 60))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_19, 0, 1, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget_5)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(0, 60))
        self.label_20.setMaximumSize(QSize(300, 60))
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_20, 0, 2, 1, 1)

        self.calib_gain5_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain5_field.setObjectName(u"calib_gain5_field")
        self.calib_gain5_field.setEnabled(True)
        self.calib_gain5_field.setMinimumSize(QSize(300, 60))
        self.calib_gain5_field.setMaximumSize(QSize(300, 60))
        self.calib_gain5_field.setFont(font1)
        self.calib_gain5_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain5_field, 6, 2, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_5)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QSize(0, 60))
        self.label_32.setMaximumSize(QSize(150, 60))
        self.label_32.setFont(font1)
        self.label_32.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setIndent(-1)

        self.gridLayout_6.addWidget(self.label_32, 5, 0, 1, 1)

        self.calib_offset1_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset1_field.setObjectName(u"calib_offset1_field")
        self.calib_offset1_field.setEnabled(True)
        self.calib_offset1_field.setMinimumSize(QSize(300, 60))
        self.calib_offset1_field.setMaximumSize(QSize(300, 60))
        self.calib_offset1_field.setFont(font1)
        self.calib_offset1_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset1_field, 2, 1, 1, 1)

        self.calib_offset5_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset5_field.setObjectName(u"calib_offset5_field")
        self.calib_offset5_field.setEnabled(True)
        self.calib_offset5_field.setMinimumSize(QSize(300, 60))
        self.calib_offset5_field.setMaximumSize(QSize(300, 60))
        self.calib_offset5_field.setFont(font1)
        self.calib_offset5_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset5_field, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 7, 1, 1, 1)

        self.comunication = QFrame(self.frame)
        self.comunication.setObjectName(u"comunication")
        self.comunication.setGeometry(QRect(0, 0, 1024, 600))
        self.comunication.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg_larger.png);\n"
"};")
        self.comunication.setFrameShape(QFrame.StyledPanel)
        self.comunication.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.comunication)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(212, 150, 600, 300))
        self.frame_13.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_13)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 601, 301))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.com_port_field = QPushButton(self.gridLayoutWidget_4)
        self.com_port_field.setObjectName(u"com_port_field")
        self.com_port_field.setEnabled(True)
        self.com_port_field.setMinimumSize(QSize(400, 75))
        self.com_port_field.setMaximumSize(QSize(200, 75))
        self.com_port_field.setFont(font2)
        self.com_port_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_5.addWidget(self.com_port_field, 1, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(0, 75))
        self.label_14.setMaximumSize(QSize(150, 75))
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setIndent(-1)

        self.gridLayout_5.addWidget(self.label_14, 0, 0, 1, 1)

        self.com_ip_field = QPushButton(self.gridLayoutWidget_4)
        self.com_ip_field.setObjectName(u"com_ip_field")
        self.com_ip_field.setEnabled(True)
        self.com_ip_field.setMinimumSize(QSize(400, 75))
        self.com_ip_field.setMaximumSize(QSize(400, 75))
        self.com_ip_field.setFont(font2)
        self.com_ip_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_5.addWidget(self.com_ip_field, 0, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setMinimumSize(QSize(0, 75))
        self.label_15.setMaximumSize(QSize(150, 75))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setIndent(-1)

        self.gridLayout_5.addWidget(self.label_15, 1, 0, 1, 1)

        self.com_back_button = QPushButton(self.gridLayoutWidget_4)
        self.com_back_button.setObjectName(u"com_back_button")
        self.com_back_button.setEnabled(True)
        self.com_back_button.setMinimumSize(QSize(200, 75))
        self.com_back_button.setMaximumSize(QSize(200, 75))
        self.com_back_button.setFont(font2)
        self.com_back_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.com_back_button.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.com_back_button, 2, 1, 1, 1, Qt.AlignRight)

        self.config = QFrame(self.frame)
        self.config.setObjectName(u"config")
        self.config.setGeometry(QRect(0, 0, 1024, 600))
        self.config.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg_larger.png);\n"
"};")
        self.config.setFrameShape(QFrame.StyledPanel)
        self.config.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.config)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(152, 85, 720, 430))
        self.frame_7.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_7)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 721, 431))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.gridLayoutWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"    selection-background-color: #B5BD00;\n"
"    background-color: #B5BD00;\n"
"   border-radius: 15px;\n"
"   border: 1px solid #B5BD00;\n"
"}\n"
"\n"
"QFrame{\n"
"   background-color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.config_data_rate_field = QComboBox(self.frame_9)
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.addItem("")
        self.config_data_rate_field.setObjectName(u"config_data_rate_field")
        self.config_data_rate_field.setGeometry(QRect(0, 10, 200, 50))
        self.config_data_rate_field.setMinimumSize(QSize(0, 50))
        self.config_data_rate_field.setMaximumSize(QSize(200, 50))
        font3 = QFont()
        font3.setPointSize(25)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setKerning(True)
        self.config_data_rate_field.setFont(font3)
        self.config_data_rate_field.setFocusPolicy(Qt.NoFocus)
        self.config_data_rate_field.setStyleSheet(u"QComboBox {\n"
"   color: rgb(0, 0, 0);\n"
"   background-color: rgb(255, 255, 255);\n"
"   border: none;\n"
"   border-radius: 15px;\n"
"    padding: 1px 0px 1px 10px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 140px;\n"
"    border:0px; /* This seems to replace the whole arrow of the combo box */\n"
"    margin-right:-47px;\n"
"    margin-left: -65px;\n"
"}\n"
"\n"
"/* Define a new custom arrow icon for the combo box */\n"
"QComboBox::down-arrow {\n"
"   image: url(:/main/arrow_down_black.png);\n"
"   width: 25px;\n"
"    height: 25px;\n"
"}")
        self.config_data_rate_field.setMaxVisibleItems(8)
        self.config_data_rate_field.setFrame(True)

        self.gridLayout.addWidget(self.frame_9, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(220, 75))
        self.label_5.setMaximumSize(QSize(600, 75))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setIndent(-1)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(220, 75))
        self.label_7.setMaximumSize(QSize(600, 75))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setIndent(-1)

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.config_aquisitions_field = QPushButton(self.gridLayoutWidget)
        self.config_aquisitions_field.setObjectName(u"config_aquisitions_field")
        self.config_aquisitions_field.setEnabled(True)
        self.config_aquisitions_field.setMinimumSize(QSize(0, 75))
        self.config_aquisitions_field.setMaximumSize(QSize(200, 75))
        self.config_aquisitions_field.setFont(font2)
        self.config_aquisitions_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.config_aquisitions_field, 2, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(220, 75))
        self.label_3.setMaximumSize(QSize(500, 75))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_3.setIndent(-1)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.config_back_button = QPushButton(self.gridLayoutWidget)
        self.config_back_button.setObjectName(u"config_back_button")
        self.config_back_button.setEnabled(True)
        self.config_back_button.setMinimumSize(QSize(0, 75))
        self.config_back_button.setMaximumSize(QSize(200, 75))
        self.config_back_button.setFont(font2)
        self.config_back_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.config_back_button.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.config_back_button, 4, 1, 1, 1)

        self.config_stabilization_field = QPushButton(self.gridLayoutWidget)
        self.config_stabilization_field.setObjectName(u"config_stabilization_field")
        self.config_stabilization_field.setEnabled(True)
        self.config_stabilization_field.setMinimumSize(QSize(0, 75))
        self.config_stabilization_field.setMaximumSize(QSize(200, 75))
        self.config_stabilization_field.setFont(font2)
        self.config_stabilization_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.config_stabilization_field, 3, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(220, 75))
        self.label_6.setMaximumSize(QSize(600, 75))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setIndent(-1)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.config_temp_ref_field = QPushButton(self.gridLayoutWidget)
        self.config_temp_ref_field.setObjectName(u"config_temp_ref_field")
        self.config_temp_ref_field.setEnabled(True)
        self.config_temp_ref_field.setMinimumSize(QSize(0, 75))
        self.config_temp_ref_field.setMaximumSize(QSize(200, 75))
        self.config_temp_ref_field.setFont(font2)
        self.config_temp_ref_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.config_temp_ref_field, 0, 1, 1, 1)

        self.keyboard = QFrame(self.frame)
        self.keyboard.setObjectName(u"keyboard")
        self.keyboard.setGeometry(QRect(0, 0, 1024, 600))
        self.keyboard.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg_larger.png);\n"
"};")
        self.keyboard.setFrameShape(QFrame.StyledPanel)
        self.keyboard.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.keyboard)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(182, 60, 660, 480))
        self.frame_15.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(23, 23, 23);\n"
"   border-radius: 35px;\n"
"};")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.frame_15)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(40, 30, 581, 421))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.keyboard_field = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.keyboard_field.setObjectName(u"keyboard_field")
        self.keyboard_field.setMinimumSize(QSize(400, 0))
        self.keyboard_field.setMaximumSize(QSize(400, 75))
        font4 = QFont()
        font4.setPointSize(40)
        self.keyboard_field.setFont(font4)
        self.keyboard_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"padding-left: 15px;")
        self.keyboard_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.keyboard_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout_11.addWidget(self.keyboard_field, 0, 0, 1, 1)

        self.keyboard_del = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_del.setObjectName(u"keyboard_del")
        self.keyboard_del.setEnabled(True)
        self.keyboard_del.setMinimumSize(QSize(120, 75))
        self.keyboard_del.setMaximumSize(QSize(120, 75))
        self.keyboard_del.setFont(font2)
        self.keyboard_del.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_del.setIconSize(QSize(25, 25))

        self.gridLayout_11.addWidget(self.keyboard_del, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_11)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.keyboard_9 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_9.setObjectName(u"keyboard_9")
        self.keyboard_9.setEnabled(True)
        self.keyboard_9.setMinimumSize(QSize(120, 75))
        self.keyboard_9.setMaximumSize(QSize(120, 75))
        self.keyboard_9.setFont(font2)
        self.keyboard_9.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_9.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_9, 0, 2, 1, 1)

        self.keyboard_4 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_4.setObjectName(u"keyboard_4")
        self.keyboard_4.setEnabled(True)
        self.keyboard_4.setMinimumSize(QSize(120, 75))
        self.keyboard_4.setMaximumSize(QSize(120, 75))
        self.keyboard_4.setFont(font2)
        self.keyboard_4.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_4.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_4, 1, 0, 1, 1)

        self.keyboard_enter = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_enter.setObjectName(u"keyboard_enter")
        self.keyboard_enter.setEnabled(True)
        self.keyboard_enter.setMinimumSize(QSize(120, 75))
        self.keyboard_enter.setMaximumSize(QSize(120, 75))
        self.keyboard_enter.setFont(font2)
        self.keyboard_enter.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_enter.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_enter, 3, 3, 1, 1)

        self.keyboard_2 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_2.setObjectName(u"keyboard_2")
        self.keyboard_2.setEnabled(True)
        self.keyboard_2.setMinimumSize(QSize(120, 75))
        self.keyboard_2.setMaximumSize(QSize(120, 75))
        self.keyboard_2.setFont(font2)
        self.keyboard_2.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_2.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_2, 2, 1, 1, 1)

        self.keyboard_5 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_5.setObjectName(u"keyboard_5")
        self.keyboard_5.setEnabled(True)
        self.keyboard_5.setMinimumSize(QSize(120, 75))
        self.keyboard_5.setMaximumSize(QSize(120, 75))
        self.keyboard_5.setFont(font2)
        self.keyboard_5.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_5.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_5, 1, 1, 1, 1)

        self.keyboard_8 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_8.setObjectName(u"keyboard_8")
        self.keyboard_8.setEnabled(True)
        self.keyboard_8.setMinimumSize(QSize(120, 75))
        self.keyboard_8.setMaximumSize(QSize(120, 75))
        self.keyboard_8.setFont(font2)
        self.keyboard_8.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_8.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_8, 0, 1, 1, 1)

        self.keyboard_ohm = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_ohm.setObjectName(u"keyboard_ohm")
        self.keyboard_ohm.setEnabled(True)
        self.keyboard_ohm.setMinimumSize(QSize(120, 75))
        self.keyboard_ohm.setMaximumSize(QSize(120, 75))
        self.keyboard_ohm.setFont(font2)
        self.keyboard_ohm.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_ohm.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_ohm, 2, 3, 1, 1)

        self.keyboard_micro = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_micro.setObjectName(u"keyboard_micro")
        self.keyboard_micro.setEnabled(True)
        self.keyboard_micro.setMinimumSize(QSize(120, 75))
        self.keyboard_micro.setMaximumSize(QSize(120, 75))
        self.keyboard_micro.setFont(font2)
        self.keyboard_micro.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_micro.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_micro, 0, 3, 1, 1)

        self.keyboard_7 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_7.setObjectName(u"keyboard_7")
        self.keyboard_7.setEnabled(True)
        self.keyboard_7.setMinimumSize(QSize(120, 75))
        self.keyboard_7.setMaximumSize(QSize(120, 75))
        self.keyboard_7.setFont(font2)
        self.keyboard_7.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_7.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_7, 0, 0, 1, 1)

        self.keyboard_6 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_6.setObjectName(u"keyboard_6")
        self.keyboard_6.setEnabled(True)
        self.keyboard_6.setMinimumSize(QSize(120, 75))
        self.keyboard_6.setMaximumSize(QSize(120, 75))
        self.keyboard_6.setFont(font2)
        self.keyboard_6.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_6.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_6, 1, 2, 1, 1)

        self.keyboard_3 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_3.setObjectName(u"keyboard_3")
        self.keyboard_3.setEnabled(True)
        self.keyboard_3.setMinimumSize(QSize(120, 75))
        self.keyboard_3.setMaximumSize(QSize(120, 75))
        self.keyboard_3.setFont(font2)
        self.keyboard_3.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_3.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_3, 2, 2, 1, 1)

        self.keyboard_1 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_1.setObjectName(u"keyboard_1")
        self.keyboard_1.setEnabled(True)
        self.keyboard_1.setMinimumSize(QSize(120, 75))
        self.keyboard_1.setMaximumSize(QSize(120, 75))
        self.keyboard_1.setFont(font2)
        self.keyboard_1.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_1.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_1, 2, 0, 1, 1)

        self.keyboard_mili = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_mili.setObjectName(u"keyboard_mili")
        self.keyboard_mili.setEnabled(True)
        self.keyboard_mili.setMinimumSize(QSize(120, 75))
        self.keyboard_mili.setMaximumSize(QSize(120, 75))
        self.keyboard_mili.setFont(font2)
        self.keyboard_mili.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_mili.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_mili, 1, 3, 1, 1)

        self.keyboard_minus = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_minus.setObjectName(u"keyboard_minus")
        self.keyboard_minus.setEnabled(True)
        self.keyboard_minus.setMinimumSize(QSize(120, 75))
        self.keyboard_minus.setMaximumSize(QSize(120, 75))
        self.keyboard_minus.setFont(font2)
        self.keyboard_minus.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_minus.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_minus, 3, 2, 1, 1)

        self.keyboard_dot = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_dot.setObjectName(u"keyboard_dot")
        self.keyboard_dot.setEnabled(True)
        self.keyboard_dot.setMinimumSize(QSize(120, 75))
        self.keyboard_dot.setMaximumSize(QSize(120, 75))
        self.keyboard_dot.setFont(font2)
        self.keyboard_dot.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_dot.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_dot, 3, 0, 1, 1)

        self.keyboard_0 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_0.setObjectName(u"keyboard_0")
        self.keyboard_0.setEnabled(True)
        self.keyboard_0.setMinimumSize(QSize(120, 75))
        self.keyboard_0.setMaximumSize(QSize(120, 75))
        self.keyboard_0.setFont(font2)
        self.keyboard_0.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_0.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_0, 3, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.main = QFrame(self.frame)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(0, 0, 1024, 600))
        font5 = QFont()
        font5.setPointSize(6)
        self.main.setFont(font5)
        self.main.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg_larger.png);\n"
"   background-color:rgb(32, 32, 32);\n"
"}")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(320, 40, 581, 521))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 340, 581, 183))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_resistance_field = QPushButton(self.verticalLayoutWidget_2)
        self.main_resistance_field.setObjectName(u"main_resistance_field")
        self.main_resistance_field.setEnabled(True)
        self.main_resistance_field.setMinimumSize(QSize(579, 100))
        self.main_resistance_field.setMaximumSize(QSize(579, 100))
        font6 = QFont()
        font6.setPointSize(70)
        font6.setBold(True)
        font6.setWeight(75)
        self.main_resistance_field.setFont(font6)
        self.main_resistance_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.verticalLayout_2.addWidget(self.main_resistance_field)

        self.main_test_button = QPushButton(self.verticalLayoutWidget_2)
        self.main_test_button.setObjectName(u"main_test_button")
        self.main_test_button.setEnabled(True)
        self.main_test_button.setMinimumSize(QSize(220, 75))
        self.main_test_button.setMaximumSize(QSize(200, 75))
        font7 = QFont()
        font7.setPointSize(30)
        font7.setBold(True)
        font7.setWeight(75)
        self.main_test_button.setFont(font7)
        self.main_test_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")

        self.verticalLayout_2.addWidget(self.main_test_button, 0, Qt.AlignRight)

        self.relative_test_frame = QFrame(self.frame_2)
        self.relative_test_frame.setObjectName(u"relative_test_frame")
        self.relative_test_frame.setGeometry(QRect(0, 0, 581, 321))
        self.relative_test_frame.setStyleSheet(u"")
        self.relative_test_frame.setFrameShape(QFrame.StyledPanel)
        self.relative_test_frame.setFrameShadow(QFrame.Raised)
        self.formLayoutWidget = QWidget(self.relative_test_frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 581, 321))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.formLayoutWidget)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(200, 60))
        self.label_21.setMaximumSize(QSize(200, 60))
        self.label_21.setFont(font1)
        self.label_21.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setIndent(-1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.main_last_res_field = QPushButton(self.formLayoutWidget)
        self.main_last_res_field.setObjectName(u"main_last_res_field")
        self.main_last_res_field.setEnabled(True)
        self.main_last_res_field.setMinimumSize(QSize(320, 60))
        self.main_last_res_field.setMaximumSize(QSize(16777215, 60))
        font8 = QFont()
        font8.setPointSize(40)
        font8.setBold(True)
        font8.setWeight(75)
        self.main_last_res_field.setFont(font8)
        self.main_last_res_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.main_last_res_field)

        self.label_24 = QLabel(self.formLayoutWidget)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(200, 60))
        self.label_24.setMaximumSize(QSize(200, 60))
        self.label_24.setFont(font1)
        self.label_24.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setIndent(-1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_24)

        self.main_2nd_last_res_field = QPushButton(self.formLayoutWidget)
        self.main_2nd_last_res_field.setObjectName(u"main_2nd_last_res_field")
        self.main_2nd_last_res_field.setEnabled(True)
        self.main_2nd_last_res_field.setMinimumSize(QSize(320, 60))
        self.main_2nd_last_res_field.setMaximumSize(QSize(16777215, 60))
        self.main_2nd_last_res_field.setFont(font8)
        self.main_2nd_last_res_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.main_2nd_last_res_field)

        self.label_22 = QLabel(self.formLayoutWidget)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(200, 60))
        self.label_22.setMaximumSize(QSize(200, 60))
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setIndent(-1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_22)

        self.main_3rd_last_res_field = QPushButton(self.formLayoutWidget)
        self.main_3rd_last_res_field.setObjectName(u"main_3rd_last_res_field")
        self.main_3rd_last_res_field.setEnabled(True)
        self.main_3rd_last_res_field.setMinimumSize(QSize(320, 60))
        self.main_3rd_last_res_field.setMaximumSize(QSize(16777215, 60))
        self.main_3rd_last_res_field.setFont(font8)
        self.main_3rd_last_res_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.main_3rd_last_res_field)

        self.label_23 = QLabel(self.formLayoutWidget)
        self.label_23.setObjectName(u"label_23")
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setMinimumSize(QSize(200, 60))
        self.label_23.setMaximumSize(QSize(200, 60))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_23.setAlignment(Qt.AlignCenter)
        self.label_23.setIndent(-1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_23)

        self.main_last_res_error_field = QPushButton(self.formLayoutWidget)
        self.main_last_res_error_field.setObjectName(u"main_last_res_error_field")
        self.main_last_res_error_field.setEnabled(True)
        self.main_last_res_error_field.setMinimumSize(QSize(320, 60))
        self.main_last_res_error_field.setMaximumSize(QSize(16777215, 60))
        self.main_last_res_error_field.setFont(font8)
        self.main_last_res_error_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.main_last_res_error_field)

        self.label_22.raise_()
        self.label_21.raise_()
        self.main_last_res_field.raise_()
        self.label_24.raise_()
        self.main_2nd_last_res_field.raise_()
        self.main_3rd_last_res_field.raise_()
        self.label_23.raise_()
        self.main_last_res_error_field.raise_()
        self.individual_test_frame = QFrame(self.frame_2)
        self.individual_test_frame.setObjectName(u"individual_test_frame")
        self.individual_test_frame.setGeometry(QRect(0, 0, 581, 321))
        self.individual_test_frame.setStyleSheet(u"")
        self.individual_test_frame.setFrameShape(QFrame.StyledPanel)
        self.individual_test_frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.individual_test_frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 581, 321))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.main_rmax_field = QPushButton(self.gridLayoutWidget_3)
        self.main_rmax_field.setObjectName(u"main_rmax_field")
        self.main_rmax_field.setEnabled(True)
        self.main_rmax_field.setMinimumSize(QSize(320, 60))
        self.main_rmax_field.setMaximumSize(QSize(16777215, 60))
        self.main_rmax_field.setFont(font8)
        self.main_rmax_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_2.addWidget(self.main_rmax_field, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_3)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(200, 60))
        self.label.setMaximumSize(QSize(200, 60))
        self.label.setFont(font2)
        self.label.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.main_rmin_field = QPushButton(self.gridLayoutWidget_3)
        self.main_rmin_field.setObjectName(u"main_rmin_field")
        self.main_rmin_field.setEnabled(True)
        self.main_rmin_field.setMinimumSize(QSize(320, 60))
        self.main_rmin_field.setMaximumSize(QSize(16777215, 60))
        self.main_rmin_field.setFont(font8)
        self.main_rmin_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_2.addWidget(self.main_rmin_field, 1, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(200, 60))
        self.label_2.setMaximumSize(QSize(200, 60))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(-1)

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.left_bar = QFrame(self.main)
        self.left_bar.setObjectName(u"left_bar")
        self.left_bar.setGeometry(QRect(0, 0, 200, 600))
        self.left_bar.setStyleSheet(u"background: rgb(44, 43, 43);")
        self.verticalLayoutWidget = QWidget(self.left_bar)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 202, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 4, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 60))
        self.widget.setMaximumSize(QSize(200, 60))
        self.widget.setStyleSheet(u"QWidget{\n"
"   background-color: #B5BD00;\n"
"   color: rgb(255, 255, 255);\n"
"   border: 2px solid #B5BD00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(64, 64, 64);\n"
"    background-color: rgb(32,32,32);\n"
"   border: 2px solid #B5BD00;\n"
"}")
        self.main_scale_select = QComboBox(self.widget)
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.setObjectName(u"main_scale_select")
        self.main_scale_select.setGeometry(QRect(0, 30, 200, 30))
        self.main_scale_select.setMinimumSize(QSize(200, 30))
        self.main_scale_select.setMaximumSize(QSize(200, 30))
        font9 = QFont()
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setUnderline(False)
        font9.setWeight(75)
        font9.setKerning(True)
        self.main_scale_select.setFont(font9)
        self.main_scale_select.setFocusPolicy(Qt.NoFocus)
        self.main_scale_select.setStyleSheet(u"QComboBox {\n"
"   margin-top: -5px;\n"
"   color: rgb(0,0,0);\n"
"   background-color: #B5BD00;\n"
"   border: 1px solid  #B5BD00;\n"
"    padding: 0px 0px 1px 5px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 150px;\n"
"    border:0px; /* This seems to replace the whole arrow of the combo box */\n"
"    margin-right:-200px;\n"
"    margin-left: -65px;\n"
"}\n"
"\n"
"")
        self.main_scale_select.setMaxVisibleItems(9)
        self.main_scale_select.setFrame(False)
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(0, 0, 200, 30))
        self.label_25.setMinimumSize(QSize(200, 30))
        self.label_25.setMaximumSize(QSize(200, 30))
        font10 = QFont()
        font10.setPointSize(15)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_25.setFont(font10)
        self.label_25.setStyleSheet(u"QLabel{\n"
"   background-color: rgb(32, 32, 32);/*rgb(143, 38, 38);*/\n"
"   color: rgb(255, 255, 255);\n"
"   border: 2px solid #B5BD00;\n"
"};")
        self.label_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(200, 60))
        self.widget_2.setMaximumSize(QSize(200, 60))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"   background-color: #B5BD00;\n"
"   color: rgb(255, 255, 255);\n"
"   border: 2px solid #B5BD00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    selection-background-color: rgb(64, 64, 64);\n"
"    background-color: rgb(32,32,32);\n"
"   border: 2px solid #B5BD00;\n"
"}")
        self.label_26 = QLabel(self.widget_2)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 0, 200, 30))
        self.label_26.setMinimumSize(QSize(200, 30))
        self.label_26.setMaximumSize(QSize(200, 30))
        self.label_26.setFont(font10)
        self.label_26.setStyleSheet(u"QLabel{\n"
"   background-color: rgb(32, 32, 32);/*rgb(143, 38, 38);*/\n"
"   color: rgb(255, 255, 255);\n"
"   border: 2px solid #B5BD00;\n"
"};")
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.config_material_field = QComboBox(self.widget_2)
        self.config_material_field.addItem("")
        self.config_material_field.addItem("")
        self.config_material_field.addItem("")
        self.config_material_field.setObjectName(u"config_material_field")
        self.config_material_field.setGeometry(QRect(0, 30, 200, 30))
        self.config_material_field.setMinimumSize(QSize(200, 30))
        self.config_material_field.setMaximumSize(QSize(200, 30))
        self.config_material_field.setFont(font9)
        self.config_material_field.setFocusPolicy(Qt.NoFocus)
        self.config_material_field.setStyleSheet(u"QComboBox {\n"
"   margin-top: -5px;\n"
"   color: rgb(0,0,0);\n"
"   background-color: #B5BD00;\n"
"   border: 1px solid  #B5BD00;\n"
"    padding: 0px 0px 1px 5px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 150px;\n"
"    border:0px; /* This seems to replace the whole arrow of the combo box */\n"
"    margin-right:-200px;\n"
"    margin-left: -65px;\n"
"}")
        self.config_material_field.setMaxVisibleItems(9)
        self.config_material_field.setFrame(False)

        self.verticalLayout.addWidget(self.widget_2)

        self.widget_4 = QWidget(self.verticalLayoutWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(200, 60))
        self.widget_4.setMaximumSize(QSize(200, 60))
        self.widget_4.setStyleSheet(u"QWidget{\n"
"   background-color: #B5BD00;\n"
"   color: rgb(255, 255, 255);\n"
"   border: 1px solid #B5BD00;\n"
"}")
        self.label_28 = QLabel(self.widget_4)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(0, 0, 200, 30))
        self.label_28.setMinimumSize(QSize(200, 30))
        self.label_28.setMaximumSize(QSize(200, 30))
        self.label_28.setFont(font10)
        self.label_28.setStyleSheet(u"QLabel{\n"
"   background-color: rgb(32, 32, 32);/*rgb(143, 38, 38);*/\n"
"   color: rgb(255, 255, 255);\n"
"   border: 2px solid #B5BD00;\n"
"};")
        self.label_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.main_comparative_button = QPushButton(self.widget_4)
        self.main_comparative_button.setObjectName(u"main_comparative_button")
        self.main_comparative_button.setEnabled(True)
        self.main_comparative_button.setGeometry(QRect(0, 30, 200, 30))
        self.main_comparative_button.setMinimumSize(QSize(200, 30))
        self.main_comparative_button.setMaximumSize(QSize(200, 30))
        self.main_comparative_button.setFont(font1)
        self.main_comparative_button.setStyleSheet(u"QPushButton {\n"
"   margin-top: -5px;\n"
"   color: rgb(0,0,0);\n"
"   background-color:#B5BD00;\n"
"   border: 1px solid  #B5BD00;\n"
"    padding: 0px 0px 1px 5px; /* This (useless) line resolves a bug with the font color */\n"
"   text-align:left;\n"
"}")

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_3 = QWidget(self.verticalLayoutWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(200, 60))
        self.widget_3.setMaximumSize(QSize(200, 60))
        self.widget_3.setStyleSheet(u"QWidget{\n"
"   background-color: #B5BD00;\n"
"   color: rgb(255, 255, 255);\n"
"   border: 1px solid #B5BD00;\n"
"}")
        self.label_27 = QLabel(self.widget_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(0, 0, 200, 30))
        self.label_27.setMinimumSize(QSize(200, 30))
        self.label_27.setMaximumSize(QSize(200, 30))
        self.label_27.setFont(font10)
        self.label_27.setStyleSheet(u"QLabel{\n"
"   background-color: rgb(32, 32, 32);/*rgb(143, 38, 38);*/\n"
"   color: rgb(255, 255, 255);\n"
"   border: 2px solid #B5BD00;\n"
"};")
        self.label_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.setup_actual_temp_field = QPushButton(self.widget_3)
        self.setup_actual_temp_field.setObjectName(u"setup_actual_temp_field")
        self.setup_actual_temp_field.setEnabled(True)
        self.setup_actual_temp_field.setGeometry(QRect(0, 30, 200, 30))
        self.setup_actual_temp_field.setMinimumSize(QSize(200, 30))
        self.setup_actual_temp_field.setMaximumSize(QSize(200, 30))
        self.setup_actual_temp_field.setFont(font1)
        self.setup_actual_temp_field.setStyleSheet(u"QPushButton {\n"
"   margin-top: -5px;\n"
"   color: rgb(0,0,0);\n"
"   background-color:#B5BD00;\n"
"   border: 1px solid  #B5BD00;\n"
"    padding: 0px 0px 1px 5px; /* This (useless) line resolves a bug with the font color */\n"
"}")

        self.verticalLayout.addWidget(self.widget_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.main_menu_button = QPushButton(self.verticalLayoutWidget)
        self.main_menu_button.setObjectName(u"main_menu_button")
        self.main_menu_button.setEnabled(True)
        self.main_menu_button.setMaximumSize(QSize(60, 60))
        icon = QIcon()
        icon.addFile(u":/main/home_default.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/main/home_disabled.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon.addFile(u":/main/home_selected.png", QSize(), QIcon.Selected, QIcon.Off)
        self.main_menu_button.setIcon(icon)
        self.main_menu_button.setIconSize(QSize(60, 60))
        self.main_menu_button.setCheckable(False)
        self.main_menu_button.setChecked(False)
        self.main_menu_button.setAutoDefault(False)
        self.main_menu_button.setFlat(True)

        self.verticalLayout.addWidget(self.main_menu_button, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.menu = QFrame(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 1024, 600))
        self.menu.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg_larger.png);\n"
"};")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_7 = QWidget(self.menu)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(130, 120, 771, 361))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.gridLayoutWidget_7)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 150))
        self.frame_5.setMaximumSize(QSize(200, 150))
        self.frame_5.setStyleSheet(u"background: #404040;\n"
"border-radius: 15px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.menu_calib_button = QToolButton(self.frame_5)
        self.menu_calib_button.setObjectName(u"menu_calib_button")
        self.menu_calib_button.setGeometry(QRect(0, 30, 201, 101))
        self.menu_calib_button.setMaximumSize(QSize(16777215, 16777215))
        font11 = QFont()
        font11.setPointSize(20)
        font11.setBold(False)
        font11.setWeight(50)
        self.menu_calib_button.setFont(font11)
        self.menu_calib_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/main/calib.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_calib_button.setIcon(icon1)
        self.menu_calib_button.setIconSize(QSize(60, 60))
        self.menu_calib_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_9.addWidget(self.frame_5, 0, 2, 1, 1)

        self.frame_4 = QFrame(self.gridLayoutWidget_7)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(200, 150))
        self.frame_4.setMaximumSize(QSize(200, 150))
        self.frame_4.setStyleSheet(u"background: #404040;\n"
"border-radius: 15px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.menu_com_button = QToolButton(self.frame_4)
        self.menu_com_button.setObjectName(u"menu_com_button")
        self.menu_com_button.setGeometry(QRect(0, 30, 201, 101))
        self.menu_com_button.setMaximumSize(QSize(16777215, 16777215))
        self.menu_com_button.setFont(font11)
        self.menu_com_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/main/comunicacao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_com_button.setIcon(icon2)
        self.menu_com_button.setIconSize(QSize(60, 60))
        self.menu_com_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_9.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.gridLayoutWidget_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 150))
        self.frame_3.setMaximumSize(QSize(200, 150))
        self.frame_3.setStyleSheet(u"background: #404040;\n"
"border-radius: 15px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.menu_config_button = QToolButton(self.frame_3)
        self.menu_config_button.setObjectName(u"menu_config_button")
        self.menu_config_button.setGeometry(QRect(0, 30, 201, 101))
        self.menu_config_button.setMaximumSize(QSize(16777215, 16777215))
        self.menu_config_button.setFont(font11)
        self.menu_config_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/main/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_config_button.setIcon(icon3)
        self.menu_config_button.setIconSize(QSize(60, 60))
        self.menu_config_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.gridLayout_9.addWidget(self.frame_3, 0, 0, 1, 1)

        self.main_home_button = QPushButton(self.gridLayoutWidget_7)
        self.main_home_button.setObjectName(u"main_home_button")
        self.main_home_button.setEnabled(True)
        self.main_home_button.setMinimumSize(QSize(0, 75))
        self.main_home_button.setMaximumSize(QSize(200, 75))
        self.main_home_button.setFont(font2)
        self.main_home_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.main_home_button.setIconSize(QSize(25, 25))

        self.gridLayout_9.addWidget(self.main_home_button, 1, 2, 1, 1)

        self.calib_2 = QFrame(self.frame)
        self.calib_2.setObjectName(u"calib_2")
        self.calib_2.setGeometry(QRect(0, 0, 1024, 600))
        self.calib_2.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg_larger.png);\n"
"};")
        self.calib_2.setFrameShape(QFrame.StyledPanel)
        self.calib_2.setFrameShadow(QFrame.Raised)
        self.frame_17 = QFrame(self.calib_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(106, 20, 811, 551))
        self.frame_17.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_9 = QWidget(self.frame_17)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(0, 0, 811, 551))
        self.gridLayoutWidget_9.setMinimumSize(QSize(0, 50))
        self.gridLayoutWidget_9.setFont(font)
        self.gridLayout_10 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.calib_gain_temp_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_gain_temp_field.setObjectName(u"calib_gain_temp_field")
        self.calib_gain_temp_field.setEnabled(True)
        self.calib_gain_temp_field.setMinimumSize(QSize(300, 60))
        self.calib_gain_temp_field.setMaximumSize(QSize(300, 60))
        self.calib_gain_temp_field.setFont(font1)
        self.calib_gain_temp_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_gain_temp_field, 5, 2, 1, 1)

        self.label_60 = QLabel(self.gridLayoutWidget_9)
        self.label_60.setObjectName(u"label_60")
        sizePolicy.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy)
        self.label_60.setMinimumSize(QSize(0, 60))
        self.label_60.setMaximumSize(QSize(150, 60))
        self.label_60.setFont(font1)
        self.label_60.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_60.setAlignment(Qt.AlignCenter)
        self.label_60.setIndent(-1)

        self.gridLayout_10.addWidget(self.label_60, 2, 0, 1, 1)

        self.label_66 = QLabel(self.gridLayoutWidget_9)
        self.label_66.setObjectName(u"label_66")
        sizePolicy.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy)
        self.label_66.setMinimumSize(QSize(0, 60))
        self.label_66.setMaximumSize(QSize(150, 60))
        self.label_66.setFont(font1)
        self.label_66.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_66.setAlignment(Qt.AlignCenter)
        self.label_66.setIndent(-1)

        self.gridLayout_10.addWidget(self.label_66, 4, 0, 1, 1)

        self.calib_offset6_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_offset6_field.setObjectName(u"calib_offset6_field")
        self.calib_offset6_field.setEnabled(True)
        self.calib_offset6_field.setMinimumSize(QSize(300, 60))
        self.calib_offset6_field.setMaximumSize(QSize(300, 60))
        self.calib_offset6_field.setFont(font1)
        self.calib_offset6_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_offset6_field, 2, 1, 1, 1)

        self.calib_back_button = QPushButton(self.gridLayoutWidget_9)
        self.calib_back_button.setObjectName(u"calib_back_button")
        self.calib_back_button.setEnabled(True)
        self.calib_back_button.setMinimumSize(QSize(200, 75))
        self.calib_back_button.setMaximumSize(QSize(200, 75))
        self.calib_back_button.setFont(font1)
        self.calib_back_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.calib_back_button.setIconSize(QSize(25, 25))

        self.gridLayout_10.addWidget(self.calib_back_button, 7, 2, 1, 1, Qt.AlignRight)

        self.label_65 = QLabel(self.gridLayoutWidget_9)
        self.label_65.setObjectName(u"label_65")
        sizePolicy.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy)
        self.label_65.setMinimumSize(QSize(0, 60))
        self.label_65.setMaximumSize(QSize(150, 60))
        self.label_65.setFont(font1)
        self.label_65.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_65.setAlignment(Qt.AlignCenter)
        self.label_65.setIndent(-1)

        self.gridLayout_10.addWidget(self.label_65, 3, 0, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget_9)
        self.label_57.setObjectName(u"label_57")
        sizePolicy.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy)
        self.label_57.setMinimumSize(QSize(0, 60))
        self.label_57.setMaximumSize(QSize(150, 60))
        self.label_57.setFont(font1)
        self.label_57.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_57.setAlignment(Qt.AlignCenter)
        self.label_57.setIndent(-1)

        self.gridLayout_10.addWidget(self.label_57, 5, 0, 1, 1)

        self.calib_offset7_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_offset7_field.setObjectName(u"calib_offset7_field")
        self.calib_offset7_field.setEnabled(True)
        self.calib_offset7_field.setMinimumSize(QSize(300, 60))
        self.calib_offset7_field.setMaximumSize(QSize(300, 60))
        self.calib_offset7_field.setFont(font1)
        self.calib_offset7_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_offset7_field, 3, 1, 1, 1)

        self.calib_offset8_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_offset8_field.setObjectName(u"calib_offset8_field")
        self.calib_offset8_field.setEnabled(True)
        self.calib_offset8_field.setMinimumSize(QSize(300, 60))
        self.calib_offset8_field.setMaximumSize(QSize(300, 60))
        self.calib_offset8_field.setFont(font1)
        self.calib_offset8_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_offset8_field, 4, 1, 1, 1)

        self.calib_gain7_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_gain7_field.setObjectName(u"calib_gain7_field")
        self.calib_gain7_field.setEnabled(True)
        self.calib_gain7_field.setMinimumSize(QSize(300, 60))
        self.calib_gain7_field.setMaximumSize(QSize(300, 60))
        self.calib_gain7_field.setFont(font1)
        self.calib_gain7_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_gain7_field, 3, 2, 1, 1)

        self.calib_offset_temp_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_offset_temp_field.setObjectName(u"calib_offset_temp_field")
        self.calib_offset_temp_field.setEnabled(True)
        self.calib_offset_temp_field.setMinimumSize(QSize(300, 60))
        self.calib_offset_temp_field.setMaximumSize(QSize(300, 60))
        self.calib_offset_temp_field.setFont(font1)
        self.calib_offset_temp_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_offset_temp_field, 5, 1, 1, 1)

        self.label_58 = QLabel(self.gridLayoutWidget_9)
        self.label_58.setObjectName(u"label_58")
        sizePolicy.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy)
        self.label_58.setMinimumSize(QSize(0, 60))
        self.label_58.setMaximumSize(QSize(300, 60))
        self.label_58.setFont(font2)
        self.label_58.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_58.setAlignment(Qt.AlignCenter)
        self.label_58.setIndent(-1)

        self.gridLayout_10.addWidget(self.label_58, 0, 1, 1, 1)

        self.label_63 = QLabel(self.gridLayoutWidget_9)
        self.label_63.setObjectName(u"label_63")
        sizePolicy.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        self.label_63.setMinimumSize(QSize(0, 60))
        self.label_63.setMaximumSize(QSize(300, 60))
        self.label_63.setFont(font1)
        self.label_63.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_63.setAlignment(Qt.AlignCenter)
        self.label_63.setIndent(-1)

        self.gridLayout_10.addWidget(self.label_63, 0, 2, 1, 1)

        self.label_61 = QLabel(self.gridLayoutWidget_9)
        self.label_61.setObjectName(u"label_61")
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QSize(0, 60))
        self.label_61.setMaximumSize(QSize(150, 60))
        self.label_61.setFont(font1)
        self.label_61.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_61.setAlignment(Qt.AlignCenter)
        self.label_61.setIndent(-1)

        self.gridLayout_10.addWidget(self.label_61, 0, 0, 1, 1)

        self.calib_gain6_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_gain6_field.setObjectName(u"calib_gain6_field")
        self.calib_gain6_field.setEnabled(True)
        self.calib_gain6_field.setMinimumSize(QSize(300, 60))
        self.calib_gain6_field.setMaximumSize(QSize(300, 60))
        self.calib_gain6_field.setFont(font1)
        self.calib_gain6_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_gain6_field, 2, 2, 1, 1)

        self.calib_gain8_field = QPushButton(self.gridLayoutWidget_9)
        self.calib_gain8_field.setObjectName(u"calib_gain8_field")
        self.calib_gain8_field.setEnabled(True)
        self.calib_gain8_field.setMinimumSize(QSize(300, 60))
        self.calib_gain8_field.setMaximumSize(QSize(300, 60))
        self.calib_gain8_field.setFont(font1)
        self.calib_gain8_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_10.addWidget(self.calib_gain8_field, 4, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.config.raise_()
        self.keyboard.raise_()
        self.comunication.raise_()
        self.menu.raise_()
        self.calib.raise_()
        self.calib_2.raise_()
        self.main.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu_config_button.clicked.connect(self.config.raise_)
        self.menu_calib_button.clicked.connect(self.calib.raise_)
        self.menu_com_button.clicked.connect(self.comunication.raise_)
        self.calib_next_button.clicked.connect(self.calib_2.raise_)
        self.com_back_button.clicked.connect(self.menu.raise_)
        self.config_back_button.clicked.connect(self.menu.raise_)
        self.main_home_button.clicked.connect(self.main.raise_)
        self.main_menu_button.clicked.connect(self.menu.raise_)
        self.calib_back_button.clicked.connect(self.menu.raise_)

        self.config_data_rate_field.setCurrentIndex(0)
        self.main_scale_select.setCurrentIndex(0)
        self.config_material_field.setCurrentIndex(0)
        self.main_menu_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.calib_offset3_field.setText("")
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.calib_gain1_field.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Escala", None))
        self.calib_next_button.setText(QCoreApplication.translate("MainWindow", u"PR\u00d3XIMO", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.calib_gain3_field.setText("")
        self.calib_offset2_field.setText("")
        self.calib_gain4_field.setText("")
        self.calib_gain2_field.setText("")
        self.calib_offset4_field.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ganho", None))
        self.calib_gain5_field.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.calib_offset1_field.setText("")
        self.calib_offset5_field.setText("")
        self.com_port_field.setText(QCoreApplication.translate("MainWindow", u"4001", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.com_ip_field.setText(QCoreApplication.translate("MainWindow", u"192.168.0.148", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PORTA", None))
        self.com_back_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.config_data_rate_field.setItemText(0, QCoreApplication.translate("MainWindow", u"2.5 SPS", None))
        self.config_data_rate_field.setItemText(1, QCoreApplication.translate("MainWindow", u"5 SPS", None))
        self.config_data_rate_field.setItemText(2, QCoreApplication.translate("MainWindow", u"10 SPS", None))
        self.config_data_rate_field.setItemText(3, QCoreApplication.translate("MainWindow", u"15 SPS", None))
        self.config_data_rate_field.setItemText(4, QCoreApplication.translate("MainWindow", u"25 SPS", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Taxa de aquisi\u00e7\u00e3o", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tempo de estabiliza\u00e7\u00e3o", None))
        self.config_aquisitions_field.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperatura de refer\u00eancia", None))
        self.config_back_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.config_stabilization_field.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Numero de aquisi\u00e7\u00f5es", None))
        self.config_temp_ref_field.setText(QCoreApplication.translate("MainWindow", u"25 \u00baC", None))
        self.keyboard_field.setPlainText("")
        self.keyboard_del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.keyboard_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.keyboard_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.keyboard_enter.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
        self.keyboard_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.keyboard_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.keyboard_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.keyboard_ohm.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.keyboard_micro.setText(QCoreApplication.translate("MainWindow", u"u\u03a9", None))
        self.keyboard_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.keyboard_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.keyboard_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.keyboard_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.keyboard_mili.setText(QCoreApplication.translate("MainWindow", u"m\u03a9", None))
        self.keyboard_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.keyboard_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.keyboard_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.main_resistance_field.setText("")
        self.main_test_button.setText(QCoreApplication.translate("MainWindow", u"TESTAR", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"MEDI\u00c7\u00c3O 1", None))
        self.main_last_res_field.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"MEDI\u00c7\u00c3O 2", None))
        self.main_2nd_last_res_field.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"MEDI\u00c7\u00c3O 3", None))
        self.main_3rd_last_res_field.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"ERRO", None))
        self.main_last_res_error_field.setText("")
        self.main_rmax_field.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"M\u00c1XIMO", None))
        self.main_rmin_field.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u00cdNIMO", None))
        self.main_scale_select.setItemText(0, QCoreApplication.translate("MainWindow", u"AUTORANGE", None))
        self.main_scale_select.setItemText(1, QCoreApplication.translate("MainWindow", u"E1: 1,00m\u03a9", None))
        self.main_scale_select.setItemText(2, QCoreApplication.translate("MainWindow", u"E2: 10,0m\u03a9", None))
        self.main_scale_select.setItemText(3, QCoreApplication.translate("MainWindow", u"E3:  100m\u03a9", None))
        self.main_scale_select.setItemText(4, QCoreApplication.translate("MainWindow", u"E4:    1,00\u03a9", None))
        self.main_scale_select.setItemText(5, QCoreApplication.translate("MainWindow", u"E5:    10,0\u03a9", None))
        self.main_scale_select.setItemText(6, QCoreApplication.translate("MainWindow", u"E6:     100\u03a9", None))
        self.main_scale_select.setItemText(7, QCoreApplication.translate("MainWindow", u"E7:   1000\u03a9", None))
        self.main_scale_select.setItemText(8, QCoreApplication.translate("MainWindow", u"E8: 10000\u03a9", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"ESCALA:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"COMPENSA\u00c7\u00c3O:", None))
        self.config_material_field.setItemText(0, QCoreApplication.translate("MainWindow", u"NENHUMA", None))
        self.config_material_field.setItemText(1, QCoreApplication.translate("MainWindow", u"COBRE", None))
        self.config_material_field.setItemText(2, QCoreApplication.translate("MainWindow", u"ALUMINIO", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"COMPARATIVO:", None))
        self.main_comparative_button.setText(QCoreApplication.translate("MainWindow", u"RELATIVO", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"TEMPERATURA", None))
        self.setup_actual_temp_field.setText("")
        self.main_menu_button.setText("")
        self.menu_calib_button.setText(QCoreApplication.translate("MainWindow", u"Calibra\u00e7\u00e3o", None))
        self.menu_com_button.setText(QCoreApplication.translate("MainWindow", u"Comunica\u00e7\u00e3o", None))
        self.menu_config_button.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.main_home_button.setText(QCoreApplication.translate("MainWindow", u"VOLTAR", None))
        self.calib_gain_temp_field.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.calib_offset6_field.setText("")
        self.calib_back_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"TEMP", None))
        self.calib_offset7_field.setText("")
        self.calib_offset8_field.setText("")
        self.calib_gain7_field.setText("")
        self.calib_offset_temp_field.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Ganho", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Escala", None))
        self.calib_gain6_field.setText("")
        self.calib_gain8_field.setText("")
    # retranslateUi

