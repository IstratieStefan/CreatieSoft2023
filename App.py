# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UiGGPwpQ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color:rgb(67, 76, 94)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.SendButton = QPushButton(self.centralwidget)
        self.SendButton.setObjectName(u"SendButton")
        self.SendButton.setGeometry(QRect(710, 520, 61, 41))
        self.SendButton.setStyleSheet(u"\n"
"background-color:rgb(94, 129, 172);\n"
"color:rgb(236, 239, 244);\n"
"border-radius:10px;\n"
"font: 8pt \"HoloLens MDL2 Assets\";")
        self.TextInput = QTextEdit(self.centralwidget)
        self.TextInput.setObjectName(u"TextInput")
        self.TextInput.setGeometry(QRect(20, 520, 681, 41))
        self.TextInput.setStyleSheet(u"background-color:rgb(236, 239, 244);\n"
"border-radius: 10px;\n"
"color:#5e81ac;")
        self.ClearButton = QPushButton(self.centralwidget)
        self.ClearButton.setObjectName(u"ClearButton")
        self.ClearButton.setGeometry(QRect(20, 20, 121, 31))
        self.ClearButton.setStyleSheet(u"\n"
"background-color:rgb(94, 129, 172);\n"
"color:rgb(236, 239, 244);\n"
"border-radius:10px;\n"
"font: 8pt \"HoloLens MDL2 Assets\";")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(30, 60, 731, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 729, 439))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Moisil Chatbot", None))
        self.SendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.TextInput.setDocumentTitle("")
        self.ClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear Conversation", None))
    # retranslateUi

