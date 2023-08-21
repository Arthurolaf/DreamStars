
#import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem, QGraphicsRectItem,QApplication
from PySide6.QtGui import QPen, QColor, QBrush, QFont,QPolygon
from PySide6.QtCore import Qt, Signal,QPoint
import pandas as pd
import random
import os
import csv
class Cursor(QPolygon):
    def __init__(self):
        self.data = None
    def setData(self, key, value):  # real signature unknown; restored from __doc__
        self.data = {"key":key, "value":value}
        """ setData(self, key: int, value: Any) -> None """


def random_line() -> str:

    file_size = os.path.getsize("stars_name.csv")
    with open("stars_name.csv", 'rb') as f:
        while True:
            pos = random.randint(0, file_size)
            if not pos:  # the first line is chosen
                return f.readline().decode()  # return str
            f.seek(pos)  # seek to random position
            f.readline()  # skip possibly incomplete line
            line = f.readline()  # read next (full) line
            if line:
                return line.decode()


class MyView(QGraphicsView):
    itemDoubleClicked = Signal(object)
    itemSelect = Signal(object)
    itemAddWay = Signal(object)
    """
    change the QGraphicsView class
    We change only the reaction to pressing, the middle mouse button (wheel)
    And allows you to move the scene with the middle mouse wheel pressed
    """


    def mousePressEvent(self, event):
        #self.selectedItems = []
        self.start_line =  {"x":None,"y":None}
        self.end_line = {"x":None,"y":None}
        if event.button() == Qt.MouseButton.MiddleButton: # or Qt.MiddleButton
            self.__prevMousePos = event.pos()
        else:
            super(MyView, self).mousePressEvent(event)

        if event.button() == Qt.LeftButton:
            singleItem = self.itemAt(event.pos().x(), event.pos().y())

            if singleItem != None and singleItem.data(0) != 0:
                #print(round(singleItem.boundingRect().x()))

                if QApplication.keyboardModifiers() == Qt.KeyboardModifier.ShiftModifier:  # This will determine if the shift key is depressed
                    #self.itemDoubleClicked.emit(singleItem)
                    #print("yes its done")
                    # if singleItem != self.selectedItems[0] :
                    self.end_line["x"] = round(singleItem.boundingRect().x())
                    self.end_line["y"] = round(singleItem.boundingRect().y())
                    self.itemAddWay.emit(self.end_line)
                    # with open("tmp.csv", 'r') as file:
                    #     csvreader = csv.reader(file)
                    #     for row in csvreader:
                    #         print("<start>:", row)
                        #print("<end>:", self.end_line)


                else:
                    #self.selectedItems = []
                    #self.selectedItems.append(singleItem)
                    self.start_line["x"] = round(singleItem.boundingRect().x())
                    # print(round(singleItem.boundingRect().y()))
                    self.start_line["y"] = round(singleItem.boundingRect().y())
                    # row_list = [[f"{self.start_line}"]]
                    # with open('tmp.csv', 'w', newline='') as file:
                    #     writer = csv.writer(file)
                    #     writer.writerows(row_list)
                    self.itemSelect.emit(self.start_line)
                    #print("<start>:", self.start_line)
                    #print("<end>:", self.end_line)
                     #= self.start_line

                    #

                # elif self.selectedItems == []:
                #     self.selectedItems.append(singleItem)
                #     self.start_line["x"] = round(singleItem.boundingRect().x())
                #     # print(round(singleItem.boundingRect().y()))
                #     self.start_line["y"] = round(singleItem.boundingRect().y())
                #     print("<start>:", self.start_line)
                #     print("<end>:", self.end_line)
                # Возможно для подойдет только для MAC-Book

                    pass
                #elif singleItem.isSelected == False:
                    #self.end_line["x"] = round(singleItem.boundingRect().x())
                    #self.end_line["y"] = round(singleItem.boundingRect().y())
                    #pass
                    #singleItem.setSelected(True)
                    #singleItem.isSelected = True
                    #self.selectedItems.append(singleItem)
            # else:
            #     self.origin = event.pos()
            #     self.rubberBand.setGeometry(QRect(self.origin, QSize()))
            #     self.rectChanged.emit(self.rubberBand.geometry())
            #     self.rubberBand.show()
            #     self.changeRubberBand = True
            return

    def mouseMoveEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_line = self.start_line
        if event.buttons() == Qt.MouseButton.MiddleButton: # or Qt.MiddleButton
            offset = self.__prevMousePos - event.pos()
            self.__prevMousePos = event.pos()

            self.verticalScrollBar().setValue(self.verticalScrollBar().value() + offset.y())
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() + offset.x())
        else:
            super(MyView, self).mouseMoveEvent(event)
    def mouseDoubleClickEvent(self, event):
        item = self.itemAt(event.pos())
        if item is not None and item.data(0) != 0:
            self.itemDoubleClicked.emit(item)
class main_map_scen():
    """
    the main class for generating a scene for loading and saving it in the future and in the documentation we will call it a map
    """
    def __init__(self, load_game=None):
        self.load = load_game
        self.load_map()
        self.cursor = None
        self.scene = self.drow_stars()
        self.model = MyView(self.scene)
        self.scene.setSceneRect(0, 0, 1000, 1000)
        self.scene.views
        self.model.setStyleSheet("background:black;")
        self.df = None
        self.scaner(x1=200, y1=100, r1=320)
        self.scaner(x1=100, y1=300, r1=120, color=1)
        self.drow_fleet(100,100,waytype=0)
        self.drow_fleet(200, 100, waytype=1)
        self.drow_fleet(300, 100, waytype=2)
        self.drow_fleet(300, 200, waytype=3)
        self.drow_fleet(300, 300, waytype=4)
        self.drow_fleet(200, 300, waytype=5)
        self.drow_fleet(100, 300, waytype=6)
        self.drow_fleet(100, 200, waytype=7)
    def drow_path(self,x1,x2,y1,y2):

        path_way = self.scene.addLine(x1,y1,x2,y2,QPen(QColor(255, 0, 0)))
        path_way.setZValue(10)
        self.model = MyView(self.scene)
        self.model.setStyleSheet("background:black;")
    def group_path(self):
        self.path_group = self.scene.createItemGroup()
        pass
    def drow_cursor(self, remove=None):
        self.cursor = Cursor()

        self.model = MyView(self.scene)
        self.model.setStyleSheet("background:black;")

    def scaner(self, x1, y1, r1=0, color=0):
        color_table = [[88, 24, 69], [99, 99, 0]]

        likescaner = self.scene.addEllipse((x1 - (r1 // 2)), (y1 - (r1 // 2)), r1, r1,
                                      QPen(QColor(0, 0, 0, 0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
                                      QBrush(
                                          QColor(color_table[color][0], color_table[color][1], color_table[color][2])))
        likescaner.setData(0, 0)
        likescaner.setZValue(color-2)
        likescaner.setOpacity(1)
        self.model = MyView(self.scene)
        self.model.setStyleSheet("background:black;")

    def drow_selector_cursor(self, x1, y1):
        cursor = [QPoint(0 + x1, 0 + y1),
                  QPoint(2 + x1, 5 + y1),
                  QPoint(0 + x1, 4 + y1),
                  QPoint(-2 + x1, 5 + y1)]
        color = QColor(100, 100, 0, 128)
        poly_cursor = Cursor(cursor)

        ship_on_map = self.scene.addPolygon(poly_cursor,
                                            QPen(QColor(0, 0, 0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
                                            QBrush(QColor(color)))
        poly_cursor.setData(0,0)
        self.model = MyView(self.scene)
        self.model.setStyleSheet("background:black;")

    def drow_fleet(self,x1,y1,waytype=0, colort=0):
        if waytype == 0:
            points =[QPoint(0+x1, 0+y1),
                QPoint(8+x1, 0+y1),
                QPoint(0+x1, 8+y1)]
            color = QColor(250,200,50,128)
        if waytype == 1:
            points =[QPoint(5+x1, 0+y1),
                QPoint(0+x1, 5+y1),
                QPoint(10+x1, 5+y1)]
            color = QColor(250, 50, 50, 128)
        if waytype == 2:
            points = [QPoint(8 + x1, 0 + y1),
                      QPoint(8 + x1, 8 + y1),
                      QPoint(0 + x1, 0 + y1)]
            color = QColor(50, 50, 200, 128)

        if waytype == 3:
            points = [QPoint(0 + x1, 5 + y1),
                      QPoint(0 + x1, 10 + y1),
                      QPoint(0 + x1, 0 + y1)]
            color = QColor(250,200,50,128)
        if waytype == 4:
            points =[QPoint(8+x1, 8+y1),
                QPoint(0+x1, 8+y1),
                QPoint(8+x1, 0+y1)]
            color = QColor(200, 50, 50, 128)
        if waytype == 5:
            points = [QPoint(5 + x1, 5 + y1),
                      QPoint(0 + x1, 0 + y1),
                      QPoint(10 + x1, 0 + y1)]
            color = QColor(50, 50, 200, 128)
        if waytype == 6:
            points = [QPoint(0 + x1, 8 + y1),
                      QPoint(0 + x1, 0 + y1),
                      QPoint(8 + x1, 8 + y1)]
            color = QColor(250,200,50,128)
        if waytype == 7:
            points =[QPoint(0+x1, 5+y1),
                QPoint(5+x1, 0+y1),
                QPoint(5+x1, 10+y1)]
            color = QColor(200, 50, 50, 128)

        poly = QPolygon(points)
        ship_on_map = self.scene.addPolygon(poly,
                                       QPen(QColor(0, 0, 0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin),
                                       QBrush(QColor(color)))
        #poly.setZValue(302)
        self.model = MyView(self.scene)
        self.model.setStyleSheet("background:black;")


    def gen_star_data(self):
        
        """
        generates a star map returns a dataframe with the coordinates of all the stars.

        The function is written with the expectation that it is used only when creating a new map (I also plan to fix a random_seed to generate identical maps)
        """
        cordinates = {"x":[],"y":[],"r":6,"name":[]}
        #random.seed(4)
        for i in range(9):
            x = random.randint(40, 940)
            y = random.randint(40, 940)
            stline = random_line()

            #r = random.randint(2, 4)
            cordinates["x"].append(x)
            cordinates["y"].append(y)
            cordinates["name"].append(stline)
        self.df = pd.DataFrame.from_dict(cordinates)
        print(self.df)

    def save_map(self):
        self.df["id"] = "1id"
        self.df.to_stata("map.stata")    
    
    def load_map(self):
        if self.load != None:
            self.df = pd.read_stata(self.load)
        else:
            self.gen_star_data()

    def drow_stars(self):

        scene = QGraphicsScene()
        for index, row in self.df.iterrows():
            x, y = row['x'], row['y']
            r = row["r"]
            #print(x, y)
            stars = scene.addEllipse(x, y, r, r, QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(255,128,20,128)))
            stars.setZValue(300)
            stars.setFlag(QGraphicsItem.ItemIsSelectable)
            stars.isSelected()
            #spec_star = scene.addEllipse(300-r//2, 300-r//2, r, r, QPen(QColor(160,160,160), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(160,160,160,128)))
            #spec_star.setZValue(299)
            font = QFont()


            #Planets
            planet_name = scene.addText(row["name"])
            planet_name.setPos(x-30, y+10)
            planet_name.setZValue(201)
            planet_name.setDefaultTextColor(QColor(250,250,250))
            planet_name.setData(0,0)
            planet_name.setZValue(0)


            #painter.drawPolygon(poly)

            #way = scene.addLine(3,5,15,45,QPen(QColor(255, 0, 0)))

            #perpendicular = scene.addLine(7.5,6,-3,14,QPen(QColor(255, 0, 0)))
            # def paintEvent(self, event):
            #     painter = QPainter()
            #     painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
            #     painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
            #     points = [
            #         QPoint(3, 5),
            #         QPoint(3, 10),
            #         QPoint(10, 5),
            #     ]
            #     poly = QPolygon(points)
            #     painter.drawPolygon(poly)

        return scene

