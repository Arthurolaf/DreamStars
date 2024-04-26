from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QPlainTextEdit,
                                QVBoxLayout, QWidget, QProgressBar)
from PyQt5.QtCore import QProcess
import sys
import re

# A regular expression, to extract the % complete.
progress_re = re.compile("Total complete: (\d+)%")

def simple_percent_parser(output):
    """
    Matches lines using the progress_re regex,
    returning a single integer for the % progress.
    """
    m = progress_re.search(output)
    if m:
        pc_complete = m.group(1)
        return int(pc_complete)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.client = None
        self.server = None

        self.btn = QPushButton("start game")
        self.btn.pressed.connect(self.start_all)

        self.text = QPlainTextEdit()
        self.text.setReadOnly(True)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)

        l = QVBoxLayout()
        l.addWidget(self.btn)
        l.addWidget(self.progress)
        l.addWidget(self.text)

        w = QWidget()
        w.setLayout(l)

        self.setCentralWidget(w)
    def start_all(self):
        self.start_server_process()
        self.start_process()
    def message(self, s):
        self.text.appendPlainText(s)

    def message_server(self, s):
        self.text.appendPlainText(s)
    def start_process(self):
        if self.client is None:  # No process running.
            self.message("Executing process Main_window")
            self.client = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.client.readyReadStandardOutput.connect(self.client_handle_stdout)
            self.client.readyReadStandardError.connect(self.client_handle_stderr)
            self.client.stateChanged.connect(self.client_handle_state)
            self.client.finished.connect(self.client_process_finished)  # Clean up once complete.
            self.client.start("python3", ['../main_window.py'])
    def start_server_process(self):
        if self.server is None:  # No process running.
            self.message_server("Executing process server")
            self.server = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.server.readyReadStandardOutput.connect(self.server_handle_stdout)
            self.server.readyReadStandardError.connect(self.server_handle_stderr)
            self.server.stateChanged.connect(self.server_handle_state)
            self.server.finished.connect(self.server_process_finished)  # Clean up once complete.
            self.server.start("python3", ['server.py'])

    def client_handle_stderr(self):
        data = self.client.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message(stderr)

    def client_handle_stdout(self):
        data = self.client.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message(stdout)

    def client_handle_state(self, state):
        states = {
            QProcess.NotRunning: 'Client Not running',
            QProcess.Starting: 'Client Starting',
            QProcess.Running: 'Client Running',
        }
        state_name = states[state]
        self.message(f"Client state changed: {state_name}")

    def client_process_finished(self):
        self.message("Client process finished.")
        self.client = None







    def server_handle_stderr(self):
        data = self.server.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        # Extract progress if it is in the data.
        progress = simple_percent_parser(stderr)
        if progress:
            self.progress.setValue(progress)
        self.message_server(stderr)

    def server_handle_stdout(self):
        data = self.server.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.message_server(stdout)

    def server_handle_state(self, state):
        states = {
            QProcess.NotRunning: 'server Not running',
            QProcess.Starting: 'server Starting',
            QProcess.Running: 'server Running',
        }
        state_name = states[state]
        self.message_server(f"server State changed: {state_name}")

    def server_process_finished(self):
        self.message_server("server Process finished.")
        self.server = None
app = QApplication(sys.argv)

w = MainWindow()
w.show()

app.exec_()


