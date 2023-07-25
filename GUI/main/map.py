
#import sys
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QColor, QBrush
from PyQt5.QtCore import Qt
import pandas as pd
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

class genstars():
    def __init__(self):
        self.scene = self.populate()
        self.model = MyView(self.scene)
        self.scene.setSceneRect(0, 0, 1000, 1000)
        self.scene.views
        self.model.setStyleSheet("background:black;")
    def gen_star_data(self):
        """
        generates a star map returns a dataframe with the coordinates of all the stars.

        The function is written with the expectation that it is used only when creating a new map (I also plan to fix a random_seed to generate identical maps)
        """
        cordinates = {"x":[],"y":[],"r":2}
        for i in range(90):
            x = random.randint(40, 940)
            y = random.randint(40, 940)
            r = random.randint(2, 4)
            cordinates["x"].append(x)
            cordinates["y"].append(y)
        df = pd.DataFrame.from_dict(cordinates)
        return df

    def populate(self):
        # Функция наплевала объектво размного размера на подобии звезд, возвращает как сцену
        scene = QGraphicsScene()
        for index, row in self.gen_star_data().iterrows():
            x, y = row['x'], row['y']
            r = row["r"]
            rect = scene.addEllipse(x, y, r, r, QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(255,128,20,128)))
            rect.setFlag( QGraphicsItem.ItemIsSelectable )
            #print(cordinates)
        return scene
    