import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Hidenbutton import changeVisibility

import random

class MyView(QGraphicsView):
 
    def mousePressEvent(self, event):
        if event.button() == Qt.MidButton: # or Qt.MiddleButton
            self.__prevMousePos = event.pos()
        else:
            super(MyView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MidButton: # or Qt.MiddleButton
            offset = self.__prevMousePos - event.pos()
            self.__prevMousePos = event.pos()

            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + offset.y())
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + offset.x())
        else:
            super(MyView, self).mouseMoveEvent(event)

class Main_Window(QWidget):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.initUI()
	
    def initUI(self):


        def populate():
            # Функция наплевала объектво размного размера на подобии звезд, возвращает как сцену
            scene = QGraphicsScene()

            for i in range(90):
                x = random.randint(40, 940)
                y = random.randint(40, 940)
                r = random.randint(2, 4)
                rect = scene.addEllipse(x, y, r, r, QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(255,128,20,128)))
                rect.setFlag( QGraphicsItem.ItemIsSelectable )

            return scene

        scene = populate()
        scene.setSceneRect(0, 0, 1000, 1000)
        scene.views
        model2 = MyView(scene)
        model2.setStyleSheet("background:black;")

        hbox = QHBoxLayout(self)

        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        textedit = QTextEdit()
        splitter1.addWidget(topleft)
        splitter1.addWidget(model2)
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