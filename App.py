import sys
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2 import QtWidgets
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 589)
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
        self.Promt = QTextEdit(self.centralwidget)
        self.Promt.setObjectName(u"Promt")
        self.Promt.setGeometry(QRect(20, 520, 681, 41))
        self.Promt.setStyleSheet(u"background-color:rgb(236, 239, 244);\n"
"border-radius: 10px;\n"
"color:#5e81ac;")
        self.Promt.setReadOnly(False)
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
        self.Result = QLabel(self.scrollAreaWidgetContents)
        self.Result.setObjectName(u"Result")
        self.Result.setGeometry(QRect(0, 0, 731, 441))
        self.Result.setStyleSheet(u"color:rgb(236, 239, 244);\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(600, 30, 160, 22))
        self.horizontalSlider.setStyleSheet(u"color:#5e81ac;")
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(530, 30, 71, 21))
        self.label.setStyleSheet(u"color:#eceff4;\n"
"font: 75 8pt \"MS Shell Dlg 2\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        if __name__ == "__main__":
            app = QApplication(sys.argv)
            MainWindow = QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Moisil Chatbot", None))
        self.SendButton.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.Promt.setDocumentTitle("")
        self.Promt.setMarkdown("")
        self.ClearButton.setText(QCoreApplication.translate("MainWindow", u"Clear Conversation", None))
        self.Result.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Temperature", None))
    # retranslateUi
