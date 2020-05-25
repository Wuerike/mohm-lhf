# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mohom.ui'
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"background-color: rgb(50, 70, 72);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(80, 120, 411, 831))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.setup_button = QPushButton(self.verticalLayoutWidget)
        self.setup_button.setObjectName(u"setup_button")
        self.setup_button.setEnabled(True)
        self.setup_button.setMinimumSize(QSize(0, 200))
        self.setup_button.setMaximumSize(QSize(16777215, 200))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.setup_button.setFont(font)
        self.setup_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.setup_button)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.menu_button = QPushButton(self.verticalLayoutWidget)
        self.menu_button.setObjectName(u"menu_button")
        self.menu_button.setEnabled(True)
        self.menu_button.setMinimumSize(QSize(0, 200))
        self.menu_button.setMaximumSize(QSize(16777215, 200))
        self.menu_button.setFont(font)
        self.menu_button.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.menu_button)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.test_button = QPushButton(self.verticalLayoutWidget)
        self.test_button.setObjectName(u"test_button")
        self.test_button.setEnabled(True)
        self.test_button.setMinimumSize(QSize(0, 200))
        self.test_button.setMaximumSize(QSize(16777215, 200))
        self.test_button.setFont(font)
        self.test_button.setStyleSheet(u"background-color: rgb(143, 38, 38);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.test_button)

        self.verticalLayoutWidget_2 = QWidget(self.frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(590, 120, 1251, 831))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scale_select = QComboBox(self.verticalLayoutWidget_2)
        self.scale_select.addItem("")
        self.scale_select.addItem("")
        self.scale_select.addItem("")
        self.scale_select.addItem("")
        self.scale_select.addItem("")
        self.scale_select.addItem("")
        self.scale_select.addItem("")
        self.scale_select.addItem("")
        self.scale_select.setObjectName(u"scale_select")
        self.scale_select.setMinimumSize(QSize(0, 150))
        font1 = QFont()
        font1.setPointSize(50)
        font1.setBold(True)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setKerning(True)
        self.scale_select.setFont(font1)
        self.scale_select.setFocusPolicy(Qt.NoFocus)
        self.scale_select.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.scale_select.setMaxVisibleItems(8)

        self.verticalLayout_2.addWidget(self.scale_select)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.max_limit_field = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.max_limit_field.setObjectName(u"max_limit_field")
        self.max_limit_field.setEnabled(False)
        self.max_limit_field.setMinimumSize(QSize(0, 150))
        self.max_limit_field.setMaximumSize(QSize(16777215, 150))
        font2 = QFont()
        font2.setPointSize(85)
        font2.setBold(True)
        font2.setWeight(75)
        self.max_limit_field.setFont(font2)
        self.max_limit_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.max_limit_field.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_3.addWidget(self.max_limit_field, 0, 1, 1, 1)

        self.min_limit_field = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.min_limit_field.setObjectName(u"min_limit_field")
        self.min_limit_field.setEnabled(False)
        self.min_limit_field.setMinimumSize(QSize(0, 150))
        self.min_limit_field.setMaximumSize(QSize(16777215, 150))
        self.min_limit_field.setFont(font2)
        self.min_limit_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.min_limit_field.setInputMethodHints(Qt.ImhNone)

        self.gridLayout_3.addWidget(self.min_limit_field, 2, 1, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(200, 150))
        self.label_2.setMaximumSize(QSize(200, 150))
        font3 = QFont()
        font3.setPointSize(50)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setIndent(-1)

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(200, 150))
        self.label.setMaximumSize(QSize(200, 150))
        self.label.setFont(font3)
        self.label.setStyleSheet(u"background-color: rgb(137, 144, 100);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(-1)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.resistance_field = QPlainTextEdit(self.verticalLayoutWidget_2)
        self.resistance_field.setObjectName(u"resistance_field")
        self.resistance_field.setEnabled(False)
        self.resistance_field.setMinimumSize(QSize(0, 200))
        self.resistance_field.setMaximumSize(QSize(16777215, 200))
        font4 = QFont()
        font4.setPointSize(115)
        font4.setBold(True)
        font4.setWeight(75)
        self.resistance_field.setFont(font4)
        self.resistance_field.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.resistance_field.setInputMethodHints(Qt.ImhNone)

        self.verticalLayout_2.addWidget(self.resistance_field)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.scale_select.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Miliohmimetro", None))
        self.setup_button.setText(QCoreApplication.translate("MainWindow", u"SETUP", None))
        self.menu_button.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.test_button.setText(QCoreApplication.translate("MainWindow", u"TESTAR", None))
        self.scale_select.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECIONE UMA ESCALA", None))
        self.scale_select.setItemText(1, QCoreApplication.translate("MainWindow", u"ESCALA 1 - RANGE: 20u\u03a9 - 200u\u03a9", None))
        self.scale_select.setItemText(2, QCoreApplication.translate("MainWindow", u"ESCALA 2 - RANGE: 200u\u03a9 - 2m\u03a9", None))
        self.scale_select.setItemText(3, QCoreApplication.translate("MainWindow", u"ESCALA 3 - RANGE: 2m\u03a9 - 20m\u03a9", None))
        self.scale_select.setItemText(4, QCoreApplication.translate("MainWindow", u"ESCALA 4 - RANGE: 20m\u03a9 - 200m\u03a9", None))
        self.scale_select.setItemText(5, QCoreApplication.translate("MainWindow", u"ESCALA 5 - RANGE: 200m\u03a9 - 2\u03a9", None))
        self.scale_select.setItemText(6, QCoreApplication.translate("MainWindow", u"ESCALA 6 - RANGE: 2\u03a9 - 20\u03a9", None))
        self.scale_select.setItemText(7, QCoreApplication.translate("MainWindow", u"ESCALA 7 - RANGE: > 20\u03a9", None))

        self.max_limit_field.setPlainText(QCoreApplication.translate("MainWindow", u"500.05uH", None))
        self.min_limit_field.setPlainText(QCoreApplication.translate("MainWindow", u"500.05uH", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rmin", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rm\u00e1x", None))
        self.resistance_field.setPlainText(QCoreApplication.translate("MainWindow", u"500.05uH", None))
    # retranslateUi

