import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Hidenbutton import changeVisibility
from map import main_map # Импортируем сцену карты.
import random



class Main_Windows(QWidget):
    def __init__(self):
        super(Main_Windows, self).__init__()
        self.initUI()
	
    def initUI(self):
        """
        Функция отвечает за инициализацию Пользоватьского интерфейса.
        """
        # область для горизонтальной разметки.
        hbox = QHBoxLayout(self)

        # Пустой заполнитель 
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        # Пустой заполнитель 
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(main_map)
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
   ex = Main_Windows()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()