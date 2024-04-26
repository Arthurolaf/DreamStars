
#import sys
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsItem, QGraphicsEllipseItem ,QGraphicsPixmapItem,QApplication,QGraphicsPolygonItem
from PySide6.QtGui import QPen, QColor, QBrush, QFont,QPolygon,QPolygonF,QPixmap,QImage
from PySide6.QtCore import Qt, Signal,QPoint,QPointF
import pandas as pd
import random
import os
from Core.Pursuit_target import pursuit
from Core.core import GameCore
from Core.Processing import *
maincore = GameCore()
class Planet(QGraphicsEllipseItem):
    """ Переопределенный Элипс под планету"""

    def __init__(self):
        super(Planet, self).__init__()
        self.id = None
    def setId(self,id):
        self.id = id

class Planet2(QGraphicsPixmapItem):
    """ Переопределенный Элипс под планету"""

    def __init__(self):
        super(Planet2, self).__init__()
        self.id = None
    def setId(self,id):
        self.id = id

class Fleet(QGraphicsPolygonItem):
    """
    QGraphicsPolygonItem

    """
    def __init__(self):
        super(Fleet, self).__init__()

        self.id = None

    def setId(self,id):
        self.id = id

class Cursor(QPolygon):
    def __init__(self):
        self.data = None

    def setData(self, key, value):  # real signature unknown; restored from __doc__
        self.data = {"key":key, "value":value}
        """ setData(self, key: int, value: Any) -> None """



def random_line() -> str:
    path_file = "/Users/artur.abaidulov/Projects/DreamStars/data/stars_name.csv"
    file_size = os.path.getsize(path_file)
    with open(path_file, 'rb') as f:
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

                if QApplication.keyboardModifiers() == Qt.KeyboardModifier.ShiftModifier:  # This will determine if the shift key is depressed
                    self.end_line["x"] = round(singleItem.boundingRect().x())
                    self.end_line["y"] = round(singleItem.boundingRect().y())
                    self.itemAddWay.emit(self.end_line)


                else:
                    self.start_line["x"] = round(singleItem.boundingRect().x())
                    self.start_line["y"] = round(singleItem.boundingRect().y())
                    self.itemSelect.emit(self.start_line)
                    pass
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
        self.fleet_cunter = 0
        self.planet_cunter = 0
        self.load = load_game
        self.load_map()
        self.cursor = None
        self.drow_stars()
        self.model = MyView(self.scene)
        self.scene.setSceneRect(0, 0, 1000, 1000)
        self.scene.views
        self.model.setStyleSheet("background:black;")
        #self.df = None
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

    def time_print(self):
        """ test function will be die after tests"""
        bad_man = {"x": 350, "y": 200, "speed": 20}
        goodman = {"x": 400, "y": 900, "speed": 10}
        goodman_target = [1, 2]

        for i in range(1, 2):
            #time.sleep(1)

            warp_t1 = pursuit(goodman["x"], goodman["y"], goodman["speed"], goodman_target[0], goodman_target[1],
                              goodman_target[0], goodman_target[1], 0)
            warp_p1 = pursuit(bad_man["x"], bad_man["y"], bad_man["speed"], warp_t1[0], warp_t1[1], warp_t1[2],
                              warp_t1[3],
                              goodman["speed"])
            print(f"-{i} turn------------------------------------------------------------------------------------")
            #print(warp_t1)
            #print(warp_p1)

            self.drow_path(warp_t1[0], warp_t1[2], warp_t1[1], warp_t1[3], QColor(255, 0, 0))
            self.drow_fleet(warp_t1[0], warp_t1[1], waytype=6)
            self.drow_path(warp_p1[0], warp_p1[2], warp_p1[1], warp_p1[3], QColor(0, 255, 0))
            self.drow_fleet(warp_p1[0], warp_p1[1], waytype=7)
            bad_man["x"] = warp_p1[2]
            bad_man["y"] = warp_p1[3]
            goodman["x"] = warp_t1[2]
            goodman["y"] = warp_t1[3]
            #print(bad_man)
            #print(goodman)
            goodman_target = [1, 2]
            if warp_t1[0] == warp_p1[0] and warp_t1[2] == warp_p1[2]:
                print("battle")
            self.scene.update()
        print("end")


    def drow_path(self,x1,x2,y1,y2,color):
        print(x1,x2,y1,y2)
        path_way = self.scene.addLine(x1,y1,x2,y2,QPen(color))
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
            points = [QPoint(0+x1, 5+y1),
                QPoint(5+x1, 0+y1),
                QPoint(5+x1, 10+y1)]
            color = QColor(200, 50, 50, 128)

        #poly = Fleet()
        custom = []
        for n in range(len(points)):
            point = points[n]
            custom.append(QPointF(point.x(), point.y()))
            #poly.insert(n,point)
        #poly.setId(self.add_id("fleet"))
        polygon = QPolygonF(custom)

        item = Fleet()
        item.setPolygon(polygon)
        item.setPen(QPen(QColor(0, 0, 0), 0))
        item.setBrush(QBrush(QColor(color)))
        item.setPos(0, 0)
        item.setId(self.add_id("fleet"))
        self.scene.addItem(item)

        self.model = MyView(self.scene)
        self.model.setStyleSheet("background:black;")


    def gen_star_data(self):
        self.df = maincore.gen_star_data()

    def save_map(self):
        #print(self.df)
        self.df["id"] = "1id"
        self.df.to_stata("map.stata")
        self.df.to_csv("map.csv")

    def load_map(self):
        if self.load != None:
            #self.df = pd.read_stata(self.load)
            self.df = pd.read_csv(self.load)
        else:
            self.gen_star_data()
    def add_id(self,type="fleet"):

        if type == "fleet":
            self.fleet_cunter += 1
            id = "F" + str(self.fleet_cunter)

        if type == "planet":
            self.planet_cunter += 1
            id = "P" + str(self.planet_cunter)
        return id
    def remove_id(self):
        pass
    def drow_stars2(self):
        self.scene.clear()
        #self.scene = QGraphicsScene()
        for index, row in self.df.iterrows():
            x, y, r, pl_id = row['x'], row['y'],row["r"], row["id"]

            #print(x, y, r)
            elips = Planet()
            elips.setZValue(300)
            elips.setRect(x, y, r, r)
            elips.setId(self.add_id("planet"))
            elips.setBrush(QColor(255, 128, 20, 128))
            elips.setPen(QColor(255, 128, 0))
            elips.setFlag(QGraphicsItem.ItemIsSelectable)

            elips.isSelected()
            #stars = scene.addItem(elips)
            new_star = Planet2()
            image_qt = QImage("Images/empty_planet.png")
            image_qt.height()
            new_star.setPixmap(QPixmap.fromImage(image_qt))
            new_star.setZValue(400)
            new_star.setPos(x-round(image_qt.width()//2),y-round(image_qt.height()//2))
            new_star.setId(pl_id)
            #new_star.set
            #self.scene.setSceneRect(0, 0, 400, 400)
            self.scene.addItem(new_star)

            #new_star = QPixmap("../../Images/fleet_planet.png")
            #new_star.setFlag(QGraphicsItem.ItemIsSelectable)
            #stars.setZValue(300)

            #spec_star = scene.addEllipse(300-r//2, 300-r//2, r, r, QPen(QColor(160,160,160), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(160,160,160,128)))
            #spec_star.setZValue(299)
            font = QFont()


            #Planets
            planet_name = self.scene.addText(row["name"])
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

        #return scene
    def drow_stars(self):

        self.scene = QGraphicsScene()


        #return scene
