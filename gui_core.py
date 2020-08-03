# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_core_7.ui'
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
        MainWindow.resize(1024, 600)
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
        self.calib.setGeometry(QRect(191, 0, 833, 600))
        self.calib.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg.png);\n"
"};")
        self.calib.setFrameShape(QFrame.StyledPanel)
        self.calib.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.calib)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(10, 0, 811, 601))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"   background-color: none;\n"
"};")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_14)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 0, 811, 601))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.calib_back_button = QPushButton(self.gridLayoutWidget_5)
        self.calib_back_button.setObjectName(u"calib_back_button")
        self.calib_back_button.setEnabled(True)
        self.calib_back_button.setMinimumSize(QSize(200, 75))
        self.calib_back_button.setMaximumSize(QSize(200, 75))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.calib_back_button.setFont(font)
        self.calib_back_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.calib_back_button.setIconSize(QSize(25, 25))

        self.gridLayout_6.addWidget(self.calib_back_button, 7, 2, 1, 1, Qt.AlignRight)

        self.calib_gain5_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain5_field.setObjectName(u"calib_gain5_field")
        self.calib_gain5_field.setEnabled(True)
        self.calib_gain5_field.setMinimumSize(QSize(300, 75))
        self.calib_gain5_field.setMaximumSize(QSize(300, 75))
        self.calib_gain5_field.setFont(font)
        self.calib_gain5_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain5_field, 6, 2, 1, 1)

        self.label_31 = QLabel(self.gridLayoutWidget_5)
        self.label_31.setObjectName(u"label_31")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(0, 75))
        self.label_31.setMaximumSize(QSize(150, 75))
        self.label_31.setFont(font)
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

        self.calib_gain4_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain4_field.setObjectName(u"calib_gain4_field")
        self.calib_gain4_field.setEnabled(True)
        self.calib_gain4_field.setMinimumSize(QSize(300, 75))
        self.calib_gain4_field.setMaximumSize(QSize(300, 75))
        self.calib_gain4_field.setFont(font)
        self.calib_gain4_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain4_field, 5, 2, 1, 1)

        self.label_32 = QLabel(self.gridLayoutWidget_5)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QSize(0, 75))
        self.label_32.setMaximumSize(QSize(150, 75))
        self.label_32.setFont(font)
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

        self.label_16 = QLabel(self.gridLayoutWidget_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(0, 75))
        self.label_16.setMaximumSize(QSize(150, 75))
        self.label_16.setFont(font)
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

        self.calib_offset1_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset1_field.setObjectName(u"calib_offset1_field")
        self.calib_offset1_field.setEnabled(True)
        self.calib_offset1_field.setMinimumSize(QSize(300, 75))
        self.calib_offset1_field.setMaximumSize(QSize(300, 75))
        self.calib_offset1_field.setFont(font)
        self.calib_offset1_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset1_field, 2, 1, 1, 1)

        self.calib_offset4_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset4_field.setObjectName(u"calib_offset4_field")
        self.calib_offset4_field.setEnabled(True)
        self.calib_offset4_field.setMinimumSize(QSize(300, 75))
        self.calib_offset4_field.setMaximumSize(QSize(300, 75))
        self.calib_offset4_field.setFont(font)
        self.calib_offset4_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset4_field, 5, 1, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(0, 75))
        self.label_17.setMaximumSize(QSize(150, 75))
        self.label_17.setFont(font)
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

        self.label_33 = QLabel(self.gridLayoutWidget_5)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QSize(0, 75))
        self.label_33.setMaximumSize(QSize(150, 75))
        self.label_33.setFont(font)
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
        self.calib_offset3_field.setMinimumSize(QSize(300, 75))
        self.calib_offset3_field.setMaximumSize(QSize(300, 75))
        self.calib_offset3_field.setFont(font)
        self.calib_offset3_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset3_field, 4, 1, 1, 1)

        self.calib_gain3_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain3_field.setObjectName(u"calib_gain3_field")
        self.calib_gain3_field.setEnabled(True)
        self.calib_gain3_field.setMinimumSize(QSize(300, 75))
        self.calib_gain3_field.setMaximumSize(QSize(300, 75))
        self.calib_gain3_field.setFont(font)
        self.calib_gain3_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain3_field, 4, 2, 1, 1)

        self.calib_offset5_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset5_field.setObjectName(u"calib_offset5_field")
        self.calib_offset5_field.setEnabled(True)
        self.calib_offset5_field.setMinimumSize(QSize(300, 75))
        self.calib_offset5_field.setMaximumSize(QSize(300, 75))
        self.calib_offset5_field.setFont(font)
        self.calib_offset5_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset5_field, 6, 1, 1, 1)

        self.calib_gain2_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain2_field.setObjectName(u"calib_gain2_field")
        self.calib_gain2_field.setEnabled(True)
        self.calib_gain2_field.setMinimumSize(QSize(300, 75))
        self.calib_gain2_field.setMaximumSize(QSize(300, 75))
        self.calib_gain2_field.setFont(font)
        self.calib_gain2_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain2_field, 3, 2, 1, 1)

        self.calib_offset2_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_offset2_field.setObjectName(u"calib_offset2_field")
        self.calib_offset2_field.setEnabled(True)
        self.calib_offset2_field.setMinimumSize(QSize(300, 75))
        self.calib_offset2_field.setMaximumSize(QSize(300, 75))
        self.calib_offset2_field.setFont(font)
        self.calib_offset2_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_offset2_field, 3, 1, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(0, 75))
        self.label_18.setMaximumSize(QSize(150, 75))
        self.label_18.setFont(font)
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

        self.label_19 = QLabel(self.gridLayoutWidget_5)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(0, 75))
        self.label_19.setMaximumSize(QSize(300, 75))
        self.label_19.setFont(font)
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
        self.label_20.setMinimumSize(QSize(0, 75))
        self.label_20.setMaximumSize(QSize(300, 75))
        self.label_20.setFont(font)
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

        self.calib_gain1_field = QPushButton(self.gridLayoutWidget_5)
        self.calib_gain1_field.setObjectName(u"calib_gain1_field")
        self.calib_gain1_field.setEnabled(True)
        self.calib_gain1_field.setMinimumSize(QSize(300, 75))
        self.calib_gain1_field.setMaximumSize(QSize(300, 75))
        self.calib_gain1_field.setFont(font)
        self.calib_gain1_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_6.addWidget(self.calib_gain1_field, 2, 2, 1, 1)

        self.comunication = QFrame(self.frame)
        self.comunication.setObjectName(u"comunication")
        self.comunication.setGeometry(QRect(191, 0, 833, 600))
        self.comunication.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg.png);\n"
"};")
        self.comunication.setFrameShape(QFrame.StyledPanel)
        self.comunication.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.comunication)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(120, 150, 601, 301))
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
        self.com_port_field.setFont(font)
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
        self.label_14.setFont(font)
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
        self.com_ip_field.setFont(font)
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
        self.label_15.setFont(font)
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
        self.com_back_button.setFont(font)
        self.com_back_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.com_back_button.setIconSize(QSize(25, 25))

        self.gridLayout_5.addWidget(self.com_back_button, 2, 1, 1, 1, Qt.AlignRight)

        self.config = QFrame(self.frame)
        self.config.setObjectName(u"config")
        self.config.setGeometry(QRect(191, 0, 833, 600))
        self.config.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg.png);\n"
"};")
        self.config.setFrameShape(QFrame.StyledPanel)
        self.config.setFrameShadow(QFrame.Raised)
        self.frame_7 = QFrame(self.config)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(60, 60, 721, 481))
        self.frame_7.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_7)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 721, 482))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(220, 75))
        self.label_5.setMaximumSize(QSize(600, 75))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_5.setIndent(-1)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(220, 75))
        self.label_6.setMaximumSize(QSize(600, 75))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setIndent(-1)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(220, 75))
        self.label_4.setMaximumSize(QSize(600, 75))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_4.setIndent(-1)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.config_temp_ref_field = QPushButton(self.gridLayoutWidget)
        self.config_temp_ref_field.setObjectName(u"config_temp_ref_field")
        self.config_temp_ref_field.setEnabled(True)
        self.config_temp_ref_field.setMinimumSize(QSize(0, 75))
        self.config_temp_ref_field.setMaximumSize(QSize(200, 75))
        self.config_temp_ref_field.setFont(font)
        self.config_temp_ref_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.config_temp_ref_field, 0, 1, 1, 1)

        self.config_stabilization_field = QPushButton(self.gridLayoutWidget)
        self.config_stabilization_field.setObjectName(u"config_stabilization_field")
        self.config_stabilization_field.setEnabled(True)
        self.config_stabilization_field.setMinimumSize(QSize(0, 75))
        self.config_stabilization_field.setMaximumSize(QSize(200, 75))
        self.config_stabilization_field.setFont(font)
        self.config_stabilization_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.config_stabilization_field, 4, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QSize(220, 75))
        self.label_7.setMaximumSize(QSize(600, 75))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_7.setIndent(-1)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.config_aquisitions_field = QPushButton(self.gridLayoutWidget)
        self.config_aquisitions_field.setObjectName(u"config_aquisitions_field")
        self.config_aquisitions_field.setEnabled(True)
        self.config_aquisitions_field.setMinimumSize(QSize(0, 75))
        self.config_aquisitions_field.setMaximumSize(QSize(200, 75))
        self.config_aquisitions_field.setFont(font)
        self.config_aquisitions_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout.addWidget(self.config_aquisitions_field, 3, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(220, 75))
        self.label_3.setMaximumSize(QSize(500, 75))
        self.label_3.setFont(font)
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
        self.config_back_button.setFont(font)
        self.config_back_button.setStyleSheet(u"background-color: #B5BD00;\n"
"color: rgb(0,0,0);\n"
"border: 1px solid #B5BD00;\n"
"border-radius: 15px;")
        self.config_back_button.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.config_back_button, 5, 1, 1, 1)

        self.frame_8 = QFrame(self.gridLayoutWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QComboBox QAbstractItemView {\n"
"    selection-background-color: #B5BD00;\n"
"    background-color: #B5BD00;\n"
"   border: 1px solid #B5BD00;\n"
"}\n"
"\n"
"QFrame{\n"
"   background-color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"}\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.config_material_field = QComboBox(self.frame_8)
        self.config_material_field.addItem("")
        self.config_material_field.addItem("")
        self.config_material_field.addItem("")
        self.config_material_field.setObjectName(u"config_material_field")
        self.config_material_field.setGeometry(QRect(0, 10, 200, 50))
        self.config_material_field.setMinimumSize(QSize(0, 50))
        self.config_material_field.setMaximumSize(QSize(200, 50))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setKerning(True)
        self.config_material_field.setFont(font1)
        self.config_material_field.setFocusPolicy(Qt.NoFocus)
        self.config_material_field.setStyleSheet(u"QComboBox {\n"
"   color: rgb(0, 0, 0);\n"
"   background-color: rgb(255, 255, 255);\n"
"   border: none;\n"
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
"}\n"
"")
        self.config_material_field.setMaxVisibleItems(8)
        self.config_material_field.setFrame(True)

        self.gridLayout.addWidget(self.frame_8, 1, 1, 1, 1)

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
        self.config_data_rate_field.setFont(font1)
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

        self.gridLayout.addWidget(self.frame_9, 2, 1, 1, 1)

        self.keyboard = QFrame(self.frame)
        self.keyboard.setObjectName(u"keyboard")
        self.keyboard.setGeometry(QRect(191, 0, 833, 600))
        self.keyboard.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg.png);\n"
"};")
        self.keyboard.setFrameShape(QFrame.StyledPanel)
        self.keyboard.setFrameShadow(QFrame.Raised)
        self.frame_15 = QFrame(self.keyboard)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(90, 50, 661, 481))
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
        self.keyboard_field = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.keyboard_field.setObjectName(u"keyboard_field")
        self.keyboard_field.setMinimumSize(QSize(541, 0))
        self.keyboard_field.setMaximumSize(QSize(541, 75))
        font2 = QFont()
        font2.setPointSize(40)
        self.keyboard_field.setFont(font2)
        self.keyboard_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"padding-left: 15px;")
        self.keyboard_field.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.keyboard_field.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout_5.addWidget(self.keyboard_field, 0, Qt.AlignHCenter)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.keyboard_micro = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_micro.setObjectName(u"keyboard_micro")
        self.keyboard_micro.setEnabled(True)
        self.keyboard_micro.setMinimumSize(QSize(120, 75))
        self.keyboard_micro.setMaximumSize(QSize(120, 75))
        self.keyboard_micro.setFont(font)
        self.keyboard_micro.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_micro.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_micro, 0, 3, 1, 1)

        self.keyboard_8 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_8.setObjectName(u"keyboard_8")
        self.keyboard_8.setEnabled(True)
        self.keyboard_8.setMinimumSize(QSize(120, 75))
        self.keyboard_8.setMaximumSize(QSize(120, 75))
        self.keyboard_8.setFont(font)
        self.keyboard_8.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_8.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_8, 0, 1, 1, 1)

        self.keyboard_5 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_5.setObjectName(u"keyboard_5")
        self.keyboard_5.setEnabled(True)
        self.keyboard_5.setMinimumSize(QSize(120, 75))
        self.keyboard_5.setMaximumSize(QSize(120, 75))
        self.keyboard_5.setFont(font)
        self.keyboard_5.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_5.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_5, 1, 1, 1, 1)

        self.keyboard_2 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_2.setObjectName(u"keyboard_2")
        self.keyboard_2.setEnabled(True)
        self.keyboard_2.setMinimumSize(QSize(120, 75))
        self.keyboard_2.setMaximumSize(QSize(120, 75))
        self.keyboard_2.setFont(font)
        self.keyboard_2.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_2.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_2, 2, 1, 1, 1)

        self.keyboard_0 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_0.setObjectName(u"keyboard_0")
        self.keyboard_0.setEnabled(True)
        self.keyboard_0.setMinimumSize(QSize(120, 75))
        self.keyboard_0.setMaximumSize(QSize(120, 75))
        self.keyboard_0.setFont(font)
        self.keyboard_0.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_0.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_0, 3, 0, 1, 1)

        self.keyboard_ohm = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_ohm.setObjectName(u"keyboard_ohm")
        self.keyboard_ohm.setEnabled(True)
        self.keyboard_ohm.setMinimumSize(QSize(120, 75))
        self.keyboard_ohm.setMaximumSize(QSize(120, 75))
        self.keyboard_ohm.setFont(font)
        self.keyboard_ohm.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_ohm.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_ohm, 2, 3, 1, 1)

        self.keyboard_6 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_6.setObjectName(u"keyboard_6")
        self.keyboard_6.setEnabled(True)
        self.keyboard_6.setMinimumSize(QSize(120, 75))
        self.keyboard_6.setMaximumSize(QSize(120, 75))
        self.keyboard_6.setFont(font)
        self.keyboard_6.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_6.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_6, 1, 2, 1, 1)

        self.keyboard_dot = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_dot.setObjectName(u"keyboard_dot")
        self.keyboard_dot.setEnabled(True)
        self.keyboard_dot.setMinimumSize(QSize(120, 75))
        self.keyboard_dot.setMaximumSize(QSize(120, 75))
        self.keyboard_dot.setFont(font)
        self.keyboard_dot.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_dot.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_dot, 3, 1, 1, 1)

        self.keyboard_9 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_9.setObjectName(u"keyboard_9")
        self.keyboard_9.setEnabled(True)
        self.keyboard_9.setMinimumSize(QSize(120, 75))
        self.keyboard_9.setMaximumSize(QSize(120, 75))
        self.keyboard_9.setFont(font)
        self.keyboard_9.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_9.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_9, 0, 2, 1, 1)

        self.keyboard_mili = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_mili.setObjectName(u"keyboard_mili")
        self.keyboard_mili.setEnabled(True)
        self.keyboard_mili.setMinimumSize(QSize(120, 75))
        self.keyboard_mili.setMaximumSize(QSize(120, 75))
        self.keyboard_mili.setFont(font)
        self.keyboard_mili.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_mili.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_mili, 1, 3, 1, 1)

        self.keyboard_del = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_del.setObjectName(u"keyboard_del")
        self.keyboard_del.setEnabled(True)
        self.keyboard_del.setMinimumSize(QSize(100, 75))
        self.keyboard_del.setMaximumSize(QSize(120, 75))
        self.keyboard_del.setFont(font)
        self.keyboard_del.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_del.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_del, 3, 2, 1, 1)

        self.keyboard_3 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_3.setObjectName(u"keyboard_3")
        self.keyboard_3.setEnabled(True)
        self.keyboard_3.setMinimumSize(QSize(120, 75))
        self.keyboard_3.setMaximumSize(QSize(120, 75))
        self.keyboard_3.setFont(font)
        self.keyboard_3.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_3.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_3, 2, 2, 1, 1)

        self.keyboard_enter = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_enter.setObjectName(u"keyboard_enter")
        self.keyboard_enter.setEnabled(True)
        self.keyboard_enter.setMinimumSize(QSize(120, 75))
        self.keyboard_enter.setMaximumSize(QSize(120, 75))
        self.keyboard_enter.setFont(font)
        self.keyboard_enter.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_enter.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_enter, 3, 3, 1, 1)

        self.keyboard_4 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_4.setObjectName(u"keyboard_4")
        self.keyboard_4.setEnabled(True)
        self.keyboard_4.setMinimumSize(QSize(120, 75))
        self.keyboard_4.setMaximumSize(QSize(120, 75))
        self.keyboard_4.setFont(font)
        self.keyboard_4.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_4.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_4, 1, 0, 1, 1)

        self.keyboard_1 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_1.setObjectName(u"keyboard_1")
        self.keyboard_1.setEnabled(True)
        self.keyboard_1.setMinimumSize(QSize(120, 75))
        self.keyboard_1.setMaximumSize(QSize(120, 75))
        self.keyboard_1.setFont(font)
        self.keyboard_1.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_1.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_1, 2, 0, 1, 1)

        self.keyboard_7 = QPushButton(self.verticalLayoutWidget_3)
        self.keyboard_7.setObjectName(u"keyboard_7")
        self.keyboard_7.setEnabled(True)
        self.keyboard_7.setMinimumSize(QSize(120, 75))
        self.keyboard_7.setMaximumSize(QSize(120, 75))
        self.keyboard_7.setFont(font)
        self.keyboard_7.setStyleSheet(u"background-color: #292929;\n"
"color: #B5BD00;\n"
"border: 1px solid #292929;\n"
"border-radius: 15px;")
        self.keyboard_7.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.keyboard_7, 0, 0, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_4)

        self.main = QFrame(self.frame)
        self.main.setObjectName(u"main")
        self.main.setGeometry(QRect(191, 0, 833, 600))
        font3 = QFont()
        font3.setPointSize(6)
        self.main.setFont(font3)
        self.main.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg.png);\n"
"};")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(130, 90, 581, 421))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 0, 582, 421))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.verticalLayoutWidget_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(580, 75))
        self.frame_6.setMaximumSize(QSize(580, 75))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.main_scale_select = QComboBox(self.frame_6)
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.addItem("")
        self.main_scale_select.setObjectName(u"main_scale_select")
        self.main_scale_select.setGeometry(QRect(0, 10, 580, 50))
        self.main_scale_select.setMinimumSize(QSize(580, 50))
        self.main_scale_select.setMaximumSize(QSize(580, 50))
        font4 = QFont()
        font4.setPointSize(30)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setWeight(75)
        font4.setKerning(True)
        self.main_scale_select.setFont(font4)
        self.main_scale_select.setFocusPolicy(Qt.NoFocus)
        self.main_scale_select.setStyleSheet(u"QComboBox {\n"
"   color: rgb(255, 255, 255);\n"
"   background-color: rgb(64, 64, 64);\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"   border-radius: 15px;\n"
"    padding: 1px 0px 1px 15px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    width: 150px;\n"
"    border:0px; /* This seems to replace the whole arrow of the combo box */\n"
"    margin-right:-47px;\n"
"    margin-left: -65px;\n"
"}\n"
"\n"
"/* Define a new custom arrow icon for the combo box */\n"
"QComboBox::down-arrow {\n"
"   image: url(:/main/arrow_down_white.png);\n"
"   width: 25px;\n"
"    height: 25px;\n"
"}\n"
"")
        self.main_scale_select.setMaxVisibleItems(8)
        self.main_scale_select.setFrame(False)

        self.verticalLayout_2.addWidget(self.frame_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_resistance_field = QPushButton(self.verticalLayoutWidget_2)
        self.main_resistance_field.setObjectName(u"main_resistance_field")
        self.main_resistance_field.setEnabled(True)
        self.main_resistance_field.setMinimumSize(QSize(300, 75))
        self.main_resistance_field.setMaximumSize(QSize(320, 75))
        font5 = QFont()
        font5.setPointSize(40)
        font5.setBold(True)
        font5.setWeight(75)
        self.main_resistance_field.setFont(font5)
        self.main_resistance_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_2.addWidget(self.main_resistance_field, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.main_rmin_field = QPushButton(self.verticalLayoutWidget_2)
        self.main_rmin_field.setObjectName(u"main_rmin_field")
        self.main_rmin_field.setEnabled(True)
        self.main_rmin_field.setMinimumSize(QSize(320, 75))
        self.main_rmin_field.setMaximumSize(QSize(200, 75))
        self.main_rmin_field.setFont(font5)
        self.main_rmin_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_2.addWidget(self.main_rmin_field, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.main_rmax_field = QPushButton(self.verticalLayoutWidget_2)
        self.main_rmax_field.setObjectName(u"main_rmax_field")
        self.main_rmax_field.setEnabled(True)
        self.main_rmax_field.setMinimumSize(QSize(320, 75))
        self.main_rmax_field.setMaximumSize(QSize(200, 75))
        self.main_rmax_field.setFont(font5)
        self.main_rmax_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_2.addWidget(self.main_rmax_field, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.main_test_button = QPushButton(self.verticalLayoutWidget_2)
        self.main_test_button.setObjectName(u"main_test_button")
        self.main_test_button.setEnabled(True)
        self.main_test_button.setMinimumSize(QSize(220, 75))
        self.main_test_button.setMaximumSize(QSize(200, 75))
        font6 = QFont()
        font6.setPointSize(30)
        font6.setBold(True)
        font6.setWeight(75)
        self.main_test_button.setFont(font6)
        self.main_test_button.setStyleSheet(u"background-color: rgb(143, 38, 38);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(143, 38, 38);\n"
"border-radius: 15px;")

        self.gridLayout_2.addWidget(self.main_test_button, 4, 0, 1, 1, Qt.AlignLeft)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(220, 75))
        self.label.setMaximumSize(QSize(220, 75))
        self.label.setFont(font6)
        self.label.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(220, 75))
        self.label_2.setMaximumSize(QSize(220, 75))
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(-1)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1, Qt.AlignLeft)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.menu = QFrame(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(191, 0, 833, 600))
        self.menu.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg.png);\n"
"};")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget = QWidget(self.menu)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 831, 599))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.horizontalLayoutWidget)
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
        font7 = QFont()
        font7.setPointSize(20)
        font7.setBold(False)
        font7.setWeight(50)
        self.menu_config_button.setFont(font7)
        self.menu_config_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/main/config.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_config_button.setIcon(icon)
        self.menu_config_button.setIconSize(QSize(60, 60))
        self.menu_config_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.horizontalLayoutWidget)
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
        self.menu_com_button.setFont(font7)
        self.menu_com_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/main/comunicacao.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_com_button.setIcon(icon1)
        self.menu_com_button.setIconSize(QSize(60, 60))
        self.menu_com_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.horizontalLayoutWidget)
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
        self.menu_calib_button.setFont(font7)
        self.menu_calib_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/main/calib.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_calib_button.setIcon(icon2)
        self.menu_calib_button.setIconSize(QSize(60, 60))
        self.menu_calib_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_2.addWidget(self.frame_5)

        self.setup = QFrame(self.frame)
        self.setup.setObjectName(u"setup")
        self.setup.setGeometry(QRect(191, 0, 833, 600))
        self.setup.setStyleSheet(u"QFrame {\n"
"   background-image: url(:/main/bg.png);\n"
"};")
        self.setup.setFrameShape(QFrame.StyledPanel)
        self.setup.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.setup)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(60, 60, 721, 481))
        self.frame_10.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"};")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_10)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 721, 482))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(220, 75))
        self.label_8.setMaximumSize(QSize(600, 75))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_8.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(220, 75))
        self.label_12.setMaximumSize(QSize(500, 75))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_12.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(220, 75))
        self.label_11.setMaximumSize(QSize(600, 75))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_11.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(220, 75))
        self.label_13.setMaximumSize(QSize(500, 75))
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_13.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(220, 75))
        self.label_10.setMaximumSize(QSize(600, 75))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.setup_stabilization_field = QPushButton(self.gridLayoutWidget_2)
        self.setup_stabilization_field.setObjectName(u"setup_stabilization_field")
        self.setup_stabilization_field.setEnabled(True)
        self.setup_stabilization_field.setMinimumSize(QSize(0, 75))
        self.setup_stabilization_field.setMaximumSize(QSize(200, 75))
        self.setup_stabilization_field.setFont(font)
        self.setup_stabilization_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_3.addWidget(self.setup_stabilization_field, 5, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(220, 75))
        self.label_9.setMaximumSize(QSize(600, 75))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"QFrame {\n"
"   background: none;\n"
"   background-color: rgb(64, 64, 64);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"   border: 1px solid  rgb(64, 64, 64);\n"
"};")
        self.label_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_9.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)

        self.setup_actual_temp_field = QPushButton(self.gridLayoutWidget_2)
        self.setup_actual_temp_field.setObjectName(u"setup_actual_temp_field")
        self.setup_actual_temp_field.setEnabled(True)
        self.setup_actual_temp_field.setMinimumSize(QSize(0, 75))
        self.setup_actual_temp_field.setMaximumSize(QSize(200, 75))
        self.setup_actual_temp_field.setFont(font)
        self.setup_actual_temp_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_3.addWidget(self.setup_actual_temp_field, 0, 1, 1, 1)

        self.setup_aquisitions_field = QPushButton(self.gridLayoutWidget_2)
        self.setup_aquisitions_field.setObjectName(u"setup_aquisitions_field")
        self.setup_aquisitions_field.setEnabled(True)
        self.setup_aquisitions_field.setMinimumSize(QSize(0, 75))
        self.setup_aquisitions_field.setMaximumSize(QSize(200, 75))
        self.setup_aquisitions_field.setFont(font)
        self.setup_aquisitions_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_3.addWidget(self.setup_aquisitions_field, 4, 1, 1, 1)

        self.frame_12 = QFrame(self.gridLayoutWidget_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setEnabled(False)
        self.frame_12.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"}\n"
"\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.setup_data_rate_field = QComboBox(self.frame_12)
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.addItem("")
        self.setup_data_rate_field.setObjectName(u"setup_data_rate_field")
        self.setup_data_rate_field.setEnabled(False)
        self.setup_data_rate_field.setGeometry(QRect(0, 20, 200, 35))
        self.setup_data_rate_field.setMinimumSize(QSize(0, 35))
        self.setup_data_rate_field.setMaximumSize(QSize(200, 35))
        self.setup_data_rate_field.setFont(font1)
        self.setup_data_rate_field.setFocusPolicy(Qt.NoFocus)
        self.setup_data_rate_field.setStyleSheet(u"QComboBox {\n"
"   color: rgb(0, 0, 0);\n"
"   background-color: rgb(255, 255, 255);\n"
"   border: none;\n"
"    padding: 1px 0px 1px 40px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border:0px; /* This seems to replace the whole arrow of the combo box */\n"
"}")
        self.setup_data_rate_field.setMaxVisibleItems(8)
        self.setup_data_rate_field.setFrame(True)

        self.gridLayout_3.addWidget(self.frame_12, 3, 1, 1, 1)

        self.frame_11 = QFrame(self.gridLayoutWidget_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setEnabled(False)
        self.frame_11.setStyleSheet(u"QFrame{\n"
"   background-color: rgb(255, 255, 255);\n"
"   border-radius: 15px;\n"
"}\n"
"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.setup_material_field = QComboBox(self.frame_11)
        self.setup_material_field.addItem("")
        self.setup_material_field.addItem("")
        self.setup_material_field.addItem("")
        self.setup_material_field.setObjectName(u"setup_material_field")
        self.setup_material_field.setEnabled(False)
        self.setup_material_field.setGeometry(QRect(0, 20, 200, 35))
        self.setup_material_field.setMinimumSize(QSize(0, 35))
        self.setup_material_field.setMaximumSize(QSize(200, 35))
        self.setup_material_field.setFont(font1)
        self.setup_material_field.setFocusPolicy(Qt.NoFocus)
        self.setup_material_field.setStyleSheet(u"QComboBox {\n"
"   color: rgb(0, 0, 0);\n"
"   background-color: rgb(255, 255, 255);\n"
"   border: none;\n"
"    padding: 1px 0px 1px 25px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border:0px; /* This seems to replace the whole arrow of the combo box */\n"
"}")
        self.setup_material_field.setMaxVisibleItems(8)
        self.setup_material_field.setFrame(True)

        self.gridLayout_3.addWidget(self.frame_11, 2, 1, 1, 1)

        self.setup_temp_ref_field = QPushButton(self.gridLayoutWidget_2)
        self.setup_temp_ref_field.setObjectName(u"setup_temp_ref_field")
        self.setup_temp_ref_field.setEnabled(True)
        self.setup_temp_ref_field.setMinimumSize(QSize(0, 75))
        self.setup_temp_ref_field.setMaximumSize(QSize(200, 75))
        self.setup_temp_ref_field.setFont(font)
        self.setup_temp_ref_field.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 15px;")

        self.gridLayout_3.addWidget(self.setup_temp_ref_field, 1, 1, 1, 1)

        self.left_bar = QFrame(self.frame)
        self.left_bar.setObjectName(u"left_bar")
        self.left_bar.setGeometry(QRect(0, 0, 190, 600))
        self.left_bar.setStyleSheet(u"background-color:rgb(44, 43, 43);\n"
"border-color: none;")
        self.left_bar.setFrameShape(QFrame.StyledPanel)
        self.left_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.left_bar)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 191, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_home_button = QPushButton(self.verticalLayoutWidget)
        self.main_home_button.setObjectName(u"main_home_button")
        self.main_home_button.setEnabled(True)
        self.main_home_button.setMaximumSize(QSize(60, 60))
        self.main_home_button.setStyleSheet(u"QPushButton:hover:!pressed\n"
"{\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/main/inicio_default.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u":/main/inicio_disabled.png", QSize(), QIcon.Disabled, QIcon.On)
        icon3.addFile(u":/main/inicio_selected.png", QSize(), QIcon.Selected, QIcon.On)
        self.main_home_button.setIcon(icon3)
        self.main_home_button.setIconSize(QSize(60, 60))
        self.main_home_button.setAutoDefault(False)
        self.main_home_button.setFlat(True)

        self.verticalLayout.addWidget(self.main_home_button, 0, Qt.AlignHCenter)

        self.main_menu_button = QPushButton(self.verticalLayoutWidget)
        self.main_menu_button.setObjectName(u"main_menu_button")
        self.main_menu_button.setEnabled(True)
        self.main_menu_button.setMaximumSize(QSize(60, 60))
        icon4 = QIcon()
        icon4.addFile(u":/main/home_default.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/main/home_disabled.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon4.addFile(u":/main/home_selected.png", QSize(), QIcon.Selected, QIcon.Off)
        self.main_menu_button.setIcon(icon4)
        self.main_menu_button.setIconSize(QSize(60, 60))
        self.main_menu_button.setCheckable(False)
        self.main_menu_button.setChecked(False)
        self.main_menu_button.setAutoDefault(False)
        self.main_menu_button.setFlat(True)

        self.verticalLayout.addWidget(self.main_menu_button, 0, Qt.AlignHCenter)

        self.main_setup_button = QPushButton(self.verticalLayoutWidget)
        self.main_setup_button.setObjectName(u"main_setup_button")
        self.main_setup_button.setEnabled(True)
        self.main_setup_button.setMaximumSize(QSize(60, 60))
        icon5 = QIcon()
        icon5.addFile(u":/main/setup_default.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/main/setup_disabled.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon5.addFile(u":/main/setup_selected.png", QSize(), QIcon.Selected, QIcon.Off)
        self.main_setup_button.setIcon(icon5)
        self.main_setup_button.setIconSize(QSize(60, 60))
        self.main_setup_button.setAutoDefault(False)
        self.main_setup_button.setFlat(True)

        self.verticalLayout.addWidget(self.main_setup_button, 0, Qt.AlignHCenter)

        self.left_bar.raise_()
        self.setup.raise_()
        self.comunication.raise_()
        self.keyboard.raise_()
        self.config.raise_()
        self.calib.raise_()
        self.menu.raise_()
        self.main.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.main_home_button.clicked.connect(self.main.raise_)
        self.main_menu_button.clicked.connect(self.menu.raise_)
        self.main_setup_button.clicked.connect(self.setup.raise_)
        self.menu_config_button.clicked.connect(self.config.raise_)
        self.menu_calib_button.clicked.connect(self.calib.raise_)
        self.menu_com_button.clicked.connect(self.comunication.raise_)
        self.calib_back_button.clicked.connect(self.menu.raise_)
        self.com_back_button.clicked.connect(self.menu.raise_)
        self.config_back_button.clicked.connect(self.menu.raise_)

        self.config_material_field.setCurrentIndex(0)
        self.config_data_rate_field.setCurrentIndex(0)
        self.main_scale_select.setCurrentIndex(0)
        self.setup_data_rate_field.setCurrentIndex(0)
        self.setup_material_field.setCurrentIndex(0)
        self.main_home_button.setDefault(False)
        self.main_menu_button.setDefault(False)
        self.main_setup_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.calib_back_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.calib_gain5_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.calib_gain4_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.calib_offset1_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.calib_offset4_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.calib_offset3_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.calib_gain3_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.calib_offset5_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.calib_gain2_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.calib_offset2_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Escala", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ganho", None))
        self.calib_gain1_field.setText(QCoreApplication.translate("MainWindow", u"0.000001", None))
        self.com_port_field.setText(QCoreApplication.translate("MainWindow", u"4001", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.com_ip_field.setText(QCoreApplication.translate("MainWindow", u"192.168.0.148", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PORTA", None))
        self.com_back_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Taxa de aquisi\u00e7\u00e3o", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Numero de aquisi\u00e7\u00f5es", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Material em teste", None))
        self.config_temp_ref_field.setText(QCoreApplication.translate("MainWindow", u"25 \u00baC", None))
        self.config_stabilization_field.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Tempo de estabiliza\u00e7\u00e3o", None))
        self.config_aquisitions_field.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperatura de refer\u00eancia", None))
        self.config_back_button.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.config_material_field.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.config_material_field.setItemText(1, QCoreApplication.translate("MainWindow", u"Cobre", None))
        self.config_material_field.setItemText(2, QCoreApplication.translate("MainWindow", u"Alum\u00ednio", None))

        self.config_data_rate_field.setItemText(0, QCoreApplication.translate("MainWindow", u"2.5 SPS", None))
        self.config_data_rate_field.setItemText(1, QCoreApplication.translate("MainWindow", u"5 SPS", None))
        self.config_data_rate_field.setItemText(2, QCoreApplication.translate("MainWindow", u"10 SPS", None))
        self.config_data_rate_field.setItemText(3, QCoreApplication.translate("MainWindow", u"15 SPS", None))
        self.config_data_rate_field.setItemText(4, QCoreApplication.translate("MainWindow", u"25 SPS", None))

        self.keyboard_field.setPlainText("")
        self.keyboard_micro.setText(QCoreApplication.translate("MainWindow", u"u\u03a9", None))
        self.keyboard_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.keyboard_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.keyboard_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.keyboard_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.keyboard_ohm.setText(QCoreApplication.translate("MainWindow", u"\u03a9", None))
        self.keyboard_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.keyboard_dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.keyboard_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.keyboard_mili.setText(QCoreApplication.translate("MainWindow", u"m\u03a9", None))
        self.keyboard_del.setText(QCoreApplication.translate("MainWindow", u"DEL", None))
        self.keyboard_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.keyboard_enter.setText(QCoreApplication.translate("MainWindow", u"ENTER", None))
        self.keyboard_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.keyboard_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.keyboard_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.main_scale_select.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE UMA ESCALA", None))
        self.main_scale_select.setItemText(1, QCoreApplication.translate("MainWindow", u"ESCALA 1: 1m\u03a9 - 10m\u03a9", None))
        self.main_scale_select.setItemText(2, QCoreApplication.translate("MainWindow", u"ESCALA 2: 10m\u03a9 - 100m\u03a9", None))
        self.main_scale_select.setItemText(3, QCoreApplication.translate("MainWindow", u"ESCALA 3: 100m\u03a9 - 1\u03a9", None))
        self.main_scale_select.setItemText(4, QCoreApplication.translate("MainWindow", u"ESCALA 4: 1\u03a9 - 10\u03a9", None))
        self.main_scale_select.setItemText(5, QCoreApplication.translate("MainWindow", u"ESCALA 5: 10\u03a9 - 100\u03a9", None))

        self.main_resistance_field.setText("")
        self.main_rmin_field.setText("")
        self.main_rmax_field.setText("")
        self.main_test_button.setText(QCoreApplication.translate("MainWindow", u"TESTAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"M\u00e1ximo:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"M\u00ednimo:", None))
        self.menu_config_button.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        self.menu_com_button.setText(QCoreApplication.translate("MainWindow", u"Comunica\u00e7\u00e3o", None))
        self.menu_calib_button.setText(QCoreApplication.translate("MainWindow", u"Calibra\u00e7\u00e3o", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Taxa de aquisi\u00e7\u00e3o", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Temperatura de refer\u00eancia", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Tempo de estabiliza\u00e7\u00e3o", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Temperatura ambiente", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Material em teste", None))
        self.setup_stabilization_field.setText(QCoreApplication.translate("MainWindow", u"0.2 s", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Numero de aquisi\u00e7\u00f5es", None))
        self.setup_actual_temp_field.setText(QCoreApplication.translate("MainWindow", u"25 \u00baC", None))
        self.setup_aquisitions_field.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.setup_data_rate_field.setItemText(0, QCoreApplication.translate("MainWindow", u"2.5 SPS", None))
        self.setup_data_rate_field.setItemText(1, QCoreApplication.translate("MainWindow", u"5.0 SPS", None))
        self.setup_data_rate_field.setItemText(2, QCoreApplication.translate("MainWindow", u"10 SPS", None))
        self.setup_data_rate_field.setItemText(3, QCoreApplication.translate("MainWindow", u"15 SPS", None))
        self.setup_data_rate_field.setItemText(4, QCoreApplication.translate("MainWindow", u"25 SPS", None))

        self.setup_material_field.setItemText(0, QCoreApplication.translate("MainWindow", u"Nenhum", None))
        self.setup_material_field.setItemText(1, QCoreApplication.translate("MainWindow", u"Cobre", None))
        self.setup_material_field.setItemText(2, QCoreApplication.translate("MainWindow", u"Alum\u00ednio", None))

        self.setup_temp_ref_field.setText(QCoreApplication.translate("MainWindow", u"25 \u00baC", None))
        self.main_home_button.setText("")
        self.main_menu_button.setText("")
        self.main_setup_button.setText("")
    # retranslateUi

