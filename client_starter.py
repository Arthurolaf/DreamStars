from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget)
from PySide6.QtCore import QProcess
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.server = None  # Default empty value.
        self.client = None

        self.btn = QPushButton("Execute")
        self.btn.pressed.connect(self.start_process)
        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)

    def message(self, s):
        self.text.appendPlainText(s)

    def start_process(self):
        if self.server is None:  # No process running.
            self.message("Executing process Server")
            self.server = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.server.finished.connect(self.server_process_finished)  # Clean up once complete.
            self.server.start("python3", ['client_server/nu_server.py'])

        if self.client is None:  # No process running.
            self.message("Executing process Client")
            self.client = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.client.finished.connect(self.client_process_finished)  # Clean up once complete.
            self.client.start("python3", ['strange/client_server/nu_client.py'])

    def server_process_finished(self):
        self.message("Server process finished.")
        self.server = None

    def client_process_finished(self):
        self.message("Client process finished.")
        self.client = None


app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec()