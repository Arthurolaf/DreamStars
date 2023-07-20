from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import Qt
import random


class MyView(QGraphicsView):
    # Artur Abaidulov -- Данная функция найдена на просторах интернета, двигает сцену средней кнопкой мыши
    
    """
    Переопределяем Нажатие клавишы средней мыши для сцены QGraphicsView
    """

    def mousePressEvent(self, event):
        """
        Функция при нажати средней клавиши мыши запоминает позицию курсора на сцене
        """
        if event.button() == Qt.MidButton: # or Qt.MiddleButton
            self.__prevMousePos = event.pos()
        else:
            super(MyView, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """
        Функция сдвигает сыену по `x` и по `y` на значение равное передвижению мыши относительно своей паследней позиции.
        Если центральная клавиша мышы нажата 
        """
        if event.buttons() == Qt.MidButton: # or Qt.MiddleButton
            offset = self.__prevMousePos - event.pos()
            self.__prevMousePos = event.pos()

            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + offset.y())
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + offset.x())
        else:
            super(MyView, self).mouseMoveEvent(event)



class GeneragteMap(QGraphicsScene):    
    def __init__(self, parent=None):        
        super(GeneragteMap, self).__init__(parent)
    
        # Функция размещения объектов размного размера на подобии звезд, возвращает как сцену
        for i in range(90):
            x = random.randint(40, 940)
            y = random.randint(40, 940)
            r = 2 #random.randint(2, 4)
            rect = self.addEllipse(x, y, r, r, QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(255,128,20,128)))
            rect.setFlag( QGraphicsItem.ItemIsSelectable )
        
        self.setSceneRect(0, 0, 1000, 1000)
        self.views
    
main_map = MyView(GeneragteMap())
main_map.setStyleSheet("background:black;")

