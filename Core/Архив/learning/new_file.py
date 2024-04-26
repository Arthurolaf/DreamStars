import threading, asyncio
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
async_loop = None
def async_setup():
     global async_loop
     async_loop = asyncio.new_event_loop()
     async_loop.run_forever()


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


        self.setWindowTitle("Async Function Example")
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login_button_clicked)

        self.setCentralWidget(w)

    async def async_login(self):
        # Perform async tasks
        print("test async button clicked!")

    def login_button_clicked(self):
        asyncio.run_coroutine_threadsafe(self.async_login(), async_loop)



async_thread = threading.Thread(target=async_setup())
async_thread.start()
app = QApplication()
window = MainWindow()
window.show()
app.exec()