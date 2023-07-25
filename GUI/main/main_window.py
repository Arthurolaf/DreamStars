import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Hidenbutton import changeVisibility
from map import main_map_scen

import random

class Main_Window(QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.initUI()
	
    def initUI(self):
        load_game = None
        
        
        hbox = QHBoxLayout(self)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)

        if load_game is not None:            
            model3 = main_map_scen(load_game=load_game)
        else:
            model3 = main_map_scen()


        splitter1.addWidget(model3.model)    
        
        splitter1.setSizes([100,200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(changeVisibility())

        hbox.addWidget(splitter2)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter demo')
        self.show()
		
def main():
   app = QApplication(sys.argv)
   ex = Main_Window()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()