
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout, QVBoxLayout,
                               QLabel, QLineEdit, QMessageBox, QPushButton,QMainWindow, QPlainTextEdit, QWidget)
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.counter = 1
        #self.server = None  # Default empty value.
        self.__setattr__(f"client{self.counter}",None)

        self.btn = QPushButton("Execute")
        self.user_label = QLabel("User Name:")
        self._user_line_edit = QLineEdit()
        self.user_label.setBuddy(self._user_line_edit)

        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.user_label)
        l.addWidget(self._user_line_edit)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        print(self.__dict__)
        #start_sting = 'main_window.py {}'.format(self._user_line_edit.text())
        start_sting = 'main_window.py'

        if self.counter <= 33:

            if self.__getattribute__(f"client{self.counter}") is None:  # No process running.
                self.message("Executing process Client")
                self.__setattr__(f"client{self.counter}",QProcess())

#                self.client = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
                self.__getattribute__(f"client{self.counter}").finished.connect(self.client_process_finished)  # Clean up once complete.
                self.__getattribute__(f"client{self.counter}").start("python3", [start_sting, self._user_line_edit.text()])

        self.counter += 1
        if self.counter <= 33:
            self.__setattr__(f"client{self.counter}", None)

    def client_process_finished(self):

        self.message("Client process finished.")
        self.client = None


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()