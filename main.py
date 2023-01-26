import sys
import openai
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton)

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

        self.setWindowTitle("Moisil Chatbot")
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.darkGray)
        self.setPalette(p)
        self.resize(800, 500)

    def on_send_clicked(self):
        text = self.line_edit.text()
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0
        )
        generated_text = completions.choices[0].text
        self.text_edit.append(text)
        self.text_edit.append(generated_text) #raspuns
        self.line_edit.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_ui = ChatUI()
    chat_ui.show()
    sys.exit(app.exec_())
