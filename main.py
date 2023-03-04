import sys
import openai
import pyttsx3
import time
engine = pyttsx3.init()
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton)
from PyQt5 import QtGui
from time import sleep
from PyQt5.QtCore import QTimer


# Set the API key
openai.api_key = "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"


class ChatUI(QWidget):
    def __init__(self):
        super().__init__()
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.line_edit = QLineEdit(self)
        self.send_button = QPushButton("Send", self)
        self.send_button.setStyleSheet(u"\n"
                                       "background-color:rgb(94, 129, 172);\n"
                                       "color:rgb(236, 239, 244);\n"
                                       "font: 8pt \"HoloLens MDL2 Assets\";")
        self.send_button.clicked.connect(self.on_send_clicked)

        layout = QVBoxLayout(self)
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.line_edit)
        h_layout.addWidget(self.send_button)
        layout.addWidget(self.text_edit)
        layout.addLayout(h_layout)
        self.setLayout(layout)

        bg_color = "#d8dee9"
        self.line_edit.setStyleSheet("background-color: {}".format(bg_color))
        self.text_edit.setStyleSheet("background-color: {}".format(bg_color))
        self.line_edit.setStyleSheet("background-color: #d8dee9;")

        self.setWindowIcon(QtGui.QIcon("moisilai.ico"))
        self.setWindowTitle("Moisil Chatbot")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor("#3b4252"))
        self.setPalette(p)
        self.resize(800, 500)

    def play_text(self,generated_text):
        engine.say(generated_text)
        engine.runAndWait()


    def on_send_clicked(self):
        text = self.line_edit.text()
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1,
        )
        generated_text = completions.choices[0].text
        self.text_edit.append("<font color='blueviolet' bgcolor='lightgrey'>" + text + "</font>")
        self.text_edit.append("<font color='black' bgcolor='white'>" + generated_text + "</font>")
        self.line_edit.clear()
        QTimer.singleShot(1, lambda: self.play_text(generated_text))
        #lasati asa

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_ui = ChatUI()
    chat_ui.show()
    sys.exit(app.exec_())
