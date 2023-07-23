import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

class MyView(QGraphicsView):
    print("test")
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

