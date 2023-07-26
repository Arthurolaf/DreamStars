import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main_window import Main_Window

class StartWindow(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        btn_layout = QHBoxLayout()
       
        btn1 = QPushButton("Start")
        btn1.setToolTip("<h3>Start new game</h3>")
        btn2 = QPushButton("Load")
        btn1.setToolTip("<h3>Load saved game</h3>")
        
        btn1.clicked.connect(self.window_start)              # <===
        btn2.clicked.connect(self.window_load)


        btn_layout.addWidget(btn1)
        btn_layout.addWidget(btn2)
        
        layout.addLayout(btn_layout)

    def window_start(self):                                             # <===
        self.w = Main_Window(load_game=None)
        self.w.show()
        self.hide()

    def window_load(self):                                             # <===
        self.w = Main_Window(load_game="map.stata")
        self.w.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication([])
    w = StartWindow()
    w.show()
    app.exec()