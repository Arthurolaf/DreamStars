from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from math import sqrt,cos,acos,asin,degrees,pi,hypot


class LogObject(QObject):
    hovered = pyqtSignal()
    notHovered = pyqtSignal()

def create_square():
    scale = 250
    path = QPainterPath()
    path.addRect(-0.076,-0.07,0.1520,0.1400)
    tr = QTransform()
    tr.scale(scale, scale)
    path = tr.map(path)
    return path

def create_circle():
    scale = 250
    path = QPainterPath()
    path.addEllipse(QPointF(0,0), 0.0750, 0.0750) # Using QPointF will center it

    tr = QTransform()
    tr.scale(scale, scale)
    path = tr.map(path)
    return path

def drawPath(x1,y1,x2,y2):
    path = QPainterPath()
    path.moveTo(x1,y1)
    path.lineTo(x2,y2)
    return path

class PathLine(QGraphicsPathItem):
    def __init__(self,x1,y1,x2,y2):
        super(PathLine,self).__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # self.name = name
        self.setFlag(QGraphicsItem.ItemIsSelectable,True)
        self.setPath(drawPath(x1,y1,x2,y2))
        self.setAcceptHoverEvents(True)
        self.log = LogObject()
        pen = QPen(Qt.white)
        pen.setStyle(Qt.SolidLine)
        pen.setWidthF(4)
        self.setPen(pen)
        self.isSelected = False
    def findLineWidth(self,zoomValue): # This function is for creating the line width value of all the drawn Objects
        if zoomValue > 18:
            zoomValue = 18
        lineWidthF = -0.0000177256625115696*(zoomValue)**4 + 0.000440875172476041*(zoomValue)**3 + 0.00941580772740735*(zoomValue)**2 - 0.370069940941448*(zoomValue) + 3
        self.updateLineWidth(lineWidthF)

    def updateLineWidth(self,lineWidth):
        pen = self.pen()
        pen.setWidthF(lineWidth)
        self.setPen(pen)

    def itemChange(self, change, value):
        if change == self.ItemSelectedChange:
            color = QColor(Qt.green) if value else QColor(Qt.white)
            pen = self.pen()
            pen.setColor(color)
            self.setPen(pen)
        return QGraphicsItem.itemChange(self, change, value)

    def hoverEnterEvent(self, event):
        color = QColor("red")
        pen = self.pen()
        pen.setColor(color)
        self.setPen(pen)
        self.log.hovered.emit()
        QGraphicsItem.hoverMoveEvent(self, event)

    def hoverLeaveEvent(self, event):
        color = QColor(Qt.green) if self.isSelected else QColor(Qt.white)
        pen = self.pen()
        pen.setColor(color)
        self.setPen(pen)
        self.log.notHovered.emit()
        QGraphicsItem.hoverMoveEvent(self, event)


class Point(QGraphicsPathItem):
    def __init__(self, x, y, r, name):
        super(Point, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.name = name
        if self.name.split('__')[1] == '0':
            self.setPath(create_circle())
        else:
            self.setPath(create_square())
        self.setScale(1.5)
        self.x = x
        self.y = y
        self.r = r
        self.setRotation(180+self.r)
        self.setAcceptHoverEvents(True)
        self.log = LogObject()
        self.setPos(x, y)
        self.isSelected = False

        pen = QPen(Qt.white)
        pen.setStyle(Qt.SolidLine)
        pen.setWidthF(3)
        self.setPen(pen)

    def findLineWidth(self,zoomValue): # This function is for creating the line width value of all the drawn Objects
        if zoomValue > 18:
            zoomValue = 18
        lineWidthF = -0.0000177256625115696*(zoomValue)**4 + 0.000440875172476041*(zoomValue)**3 + 0.00941580772740735*(zoomValue)**2 - 0.370069940941448*(zoomValue) + 3
        self.updateLineWidth(lineWidthF)

    def updateLineWidth(self,lineWidth):
        pen = self.pen()
        pen.setWidthF(lineWidth)
        self.setPen(pen)

    def itemChange(self, change, value):
        if change == self.ItemSelectedChange:
            color = QColor(Qt.green) if value else QColor(Qt.white)
            pen = self.pen()
            pen.setColor(color)
            self.setPen(pen)
        return QGraphicsItem.itemChange(self, change, value)

    def hoverEnterEvent(self, event):
        color = QColor("red")
        pen = self.pen()
        pen.setColor(color)
        self.setPen(pen)
        self.log.hovered.emit()
        QGraphicsItem.hoverMoveEvent(self, event)

    def hoverLeaveEvent(self, event):
        color = QColor(Qt.green) if self.isSelected else QColor(Qt.white)
        pen = self.pen()
        pen.setColor(color)
        self.setPen(pen)
        self.log.notHovered.emit()
        QGraphicsItem.hoverMoveEvent(self, event)

    def mouseDoubleClickEvent(self,event):
        print(self.name)

class Viewer(QGraphicsView):
    photoClicked = pyqtSignal(QPoint)
    rectChanged = pyqtSignal(QRect)

    def __init__(self, parent):
        super(Viewer, self).__init__(parent)
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.setMouseTracking(True)
        self.origin = QPoint()
        self.changeRubberBand = False
        self.setRenderHints(QPainter.Antialiasing)

        self._zoom = 0
        self._empty = True
        self.setScene(QGraphicsScene(self))

        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setFrameShape(QFrame.NoFrame)
        self.area = float()
        self.setPoints()
        self.viewport().setCursor(Qt.ArrowCursor)
        QTimer.singleShot(0, self.reset_fit)
        self.selectedItems = []
        self.setBackgroundBrush(Qt.black)


    def setItems(self):
        self.data = {
            "x": [
                -2415594.9965,
                -2414943.8686,
                -2417160.6592,
                # -2417160.6592,
                -2417856.1783,
                -2417054.7618,
                -2416009.9966,
                -2416012.5232,
                # -2418160.8952,
                -2418160.8952,
                # -2416012.5232,
                # -2417094.7694,
                -2417094.7694,
            ],
            "y": [
                10453172.2426,
                10454269.7008,
                10454147.2672,
                # 10454147.2672,
                10453285.2456,
                10452556.8132,
                10453240.2808,
                10455255.8752,
                # 10455183.1912,
                10455183.1912,
                # 10455255.8752,
                # 10456212.5959,
                10456212.5959,
            ],
            "rotation":[
            0,
            313.9962,
            43.9962,
            # 223.9962,
            227.7070,
            227.7070,
            313.9962,
            43.9962,
            # 43.9962,
            223.9962,
            # 223.9962,
            # 43.9962,
            223.9962,
            ]
        }

        self.adjustedPoints = {}
        for i, (x, y,r) in enumerate(zip(self.data["x"], self.data["y"],self.data["rotation"])):
            p = Point(x, y,r, "Point__" + str(i))
            p.log.hovered.connect(self.hoverChange)
            p.log.notHovered.connect(self.notHoverChange)
            self.scene().addItem(p)
            self.adjustedPoints[i] = [x,y]
            # if i == 0:
            #     self.adjustedPoints['c__'+str(i)] = [x,y]
            # else:
            #     self.adjustedPoints['s__'+str(i)] = [x,y]

    def drawConnectingLines(self):
        # result = self.group(self.adjustedPoints, 'c__0')
        result = self.group(self.adjustedPoints, 0)
        for startPoint in result.items():
            x1 = self.adjustedPoints[startPoint[0]][0]
            y1 = self.adjustedPoints[startPoint[0]][1]
            for endPoint in startPoint[1]:
                x2 = self.adjustedPoints[endPoint][0]
                y2 = self.adjustedPoints[endPoint][1]
                connectingLine = PathLine(x1,y1,x2,y2)
                # connectingLine.drawPath()
                self.scene().addItem(connectingLine)
                # QApplication.processEvents()
        self.scene().update()


    def findMinDistance(self,data, start):
        xStart, yStart = data[start]
        distances = []
        for item,[x,y] in data.items():
            if item != start and item != 0:
                distances.append(hypot(abs(xStart - x),abs(yStart-y)))
        output = self.mean(distances)-min(distances)
        if output < min(distances):
            output = min(distances)
        return output

    def mean(self,numbers):
        return float(sum(numbers)) / max(len(numbers), 1)


    def group(self,d, start,seen = []):
       x, y = d[start]
       r =[]
       print(start)
       dist = self.findMinDistance(d,start)
       print(dist)
       for a, [j, k] in d.items():
           if a != start and a not in seen and hypot(abs(x-j), abs(y-k)) <= dist:
               r.append(a)
       if not r:
         return {}
       result = {start:r}
       for i in r:
         result.update(self.group(d, i, seen+[start, *r]))
       return result


    def setPoints(self):
        self.setItems()
        # self.drawConnectingLines()
        self.setDragMode(self.ScrollHandDrag)

    def wheelEvent(self, event):
        for item in self.scene().items():
            item.findLineWidth(self._zoom)

        if event.angleDelta().y() > 0: # angleDelta is positive 120 zooming in and -120 going out
            factor = 1.25
            self._zoom += 1
        else:
            factor = 0.8
            self._zoom -= 1
        if self._zoom > 0:
            self.scale(factor, factor)
        elif self._zoom == 0:
            self.reset_fit()
        else:
            self._zoom = 0

    def hoverChange(self):
        self.viewport().setCursor(Qt.PointingHandCursor)

    def notHoverChange(self):
        self.viewport().setCursor(Qt.ArrowCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            singleItem = self.itemAt(event.pos().x(), event.pos().y())
            if singleItem != None:
                if QApplication.keyboardModifiers() == Qt.ShiftModifier: # This will determine if the shift key is depressed
                    if singleItem.isSelected == True:
                        singleItem.setSelected(False)
                        singleItem.isSelected = False
                        self.selectedItems.remove(singleItem)
                elif singleItem.isSelected == False:
                    singleItem.setSelected(True)
                    singleItem.isSelected = True
                    self.selectedItems.append(singleItem)
            else:
                self.origin = event.pos()
                self.rubberBand.setGeometry(QRect(self.origin, QSize()))
                self.rectChanged.emit(self.rubberBand.geometry())
                self.rubberBand.show()
                self.changeRubberBand = True
            return

        elif event.button() == Qt.MidButton:
            self.viewport().setCursor(Qt.ClosedHandCursor)
            self.original_event = event
            handmade_event = QMouseEvent(
                QEvent.MouseButtonPress,
                QPointF(event.pos()),
                Qt.LeftButton,
                event.buttons(),
                Qt.KeyboardModifiers(),
            )
            QGraphicsView.mousePressEvent(self, handmade_event)

        super(Viewer, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        point = event.pos()
        if event.button() == Qt.LeftButton:
            self.changeRubberBand = False
            if self.rubberBand.isVisible():
                self.rubberBand.hide()
                rect = self.rubberBand.geometry()
                rect_scene = self.mapToScene(rect).boundingRect()
                selected = self.scene().items(rect_scene)
                if selected:
                    # print(selected)
                    for selectedPoints in selected:
                        if QApplication.keyboardModifiers() == Qt.ShiftModifier: # This will determine if the shift key is depressed
                            if selectedPoints.isSelected == True:
                                selectedPoints.setSelected(False)
                                selectedPoints.isSelected = False
                                self.selectedItems.remove(selectedPoints)
                        elif selectedPoints.isSelected == False: # if the shif key is not depressed and its not selected, then select it
                            selectedPoints.setSelected(True)
                            selectedPoints.isSelected = True
                            self.selectedItems.append(selectedPoints)
                    print( "".join("Item: %s\n" % child.name for child in self.selectedItems))
                else:
                    print(" Nothing\n")
                    for selected in self.selectedItems:
                        selected.setSelected(False)
                        selected.isSelected = False
                    self.selectedItems.clear()
                    QGraphicsView.mouseReleaseEvent(self, event)

        elif event.button() == Qt.MidButton:
            self.viewport().setCursor(Qt.ArrowCursor)
            handmade_event = QMouseEvent(
                QEvent.MouseButtonRelease,
                QPointF(event.pos()),
                Qt.LeftButton,
                event.buttons(),
                Qt.KeyboardModifiers(),
            )
            QGraphicsView.mouseReleaseEvent(self, handmade_event)

    def mouseMoveEvent(self, event):
        if self.changeRubberBand:
            self.rubberBand.setGeometry(
                QRect(self.origin, event.pos()).normalized()
            )
            self.rectChanged.emit(self.rubberBand.geometry())
            QGraphicsView.mouseMoveEvent(self, event)
        super(Viewer, self).mouseMoveEvent(event)

    def reset_fit(self):
        r = self.scene().itemsBoundingRect()
        self.resetTransform()
        self.setSceneRect(r)
        self.fitInView(r, Qt.KeepAspectRatio)
        self._zoom = 0
        self.scale(1, -1)


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.viewer = Viewer(self)
        self.btnFindPath = QToolButton(self)
        self.btnFindPath.setText("Draw Path")
        self.btnFindPath.clicked.connect(self.autoDrawLines)

        VBlayout = QVBoxLayout(self)
        VBlayout.addWidget(self.viewer)
        HBlayout = QHBoxLayout()
        HBlayout.setAlignment(Qt.AlignLeft)
        HBlayout.addWidget(self.btnFindPath)
        VBlayout.addLayout(HBlayout)

    def autoDrawLines(self):
        self.viewer.drawConnectingLines()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 800, 600)
    window.show()
    sys.exit(app.exec_())