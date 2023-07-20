import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random


class MyGraphicsView(QGraphicsView):
    def __init__(self):
        super(MyGraphicsView, self).__init__()
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self._isPanning = False
        self._mousePressed = False
        # self.setBackgroundBrush(QImage("C:/Users/jmartini/Desktop/Temp/images/flag_0140.jpg"))
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setHorizontalScrollBarPolicy( Qt.ScrollBarAlwaysOff )
        self.setVerticalScrollBarPolicy( Qt.ScrollBarAlwaysOff )


    def mousePressEvent(self,  event):
        if event.button() == Qt.LeftButton:
            self._mousePressed = True
            if self._isPanning:
                self.setCursor(Qt.ClosedHandCursor)
                self._dragPos = event.pos()
                event.accept()
            else:
                super(MyGraphicsView, self).mousePressEvent(event)
        elif event.button() == Qt.MiddleButton:
            self._mousePressed = True
            self._isPanning = True
            self.setCursor(Qt.ClosedHandCursor)
            self._dragPos = event.pos()
            event.accept()


    def mouseMoveEvent(self, event):
        if self._mousePressed and self._isPanning:
            newPos = event.pos()
            diff = newPos - self._dragPos
            self._dragPos = newPos
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - diff.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - diff.y())
            event.accept()
        else:
            super(MyGraphicsView, self).mouseMoveEvent(event)


    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self._isPanning:
                self.setCursor(Qt.OpenHandCursor)
            else:
                self._isPanning = False
                self.setCursor(Qt.ArrowCursor)
            self._mousePressed = False
        elif event.button() == Qt.MiddleButton:
            self._isPanning = False
            self.setCursor(Qt.ArrowCursor)
            self._mousePressed = False
        super(MyGraphicsView, self).mouseReleaseEvent(event)


    def mouseDoubleClickEvent(self, event): 
        self.fitInView(self.sceneRect(), Qt.KeepAspectRatio)
        pass


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space and not self._mousePressed:
            self._isPanning = True
            self.setCursor(Qt.OpenHandCursor)
        else:
            super(MyGraphicsView, self).keyPressEvent(event)


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Space:
            if not self._mousePressed:
                self._isPanning = False
                self.setCursor(Qt.ArrowCursor)
        else:
            super(MyGraphicsView, self).keyPressEvent(event)


    def wheelEvent(self,  event):
        # zoom factor
        factor = 1.25

        # Set Anchors
        self.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.setResizeAnchor(QGraphicsView.NoAnchor)

        # Save the scene pos
        oldPos = self.mapToScene(event.pos())

        # Zoom
      #   if event.delta() < 0:
      #       factor = 1.0 / factor
      #   self.scale(factor, factor)

        # Get the new position
        newPos = self.mapToScene(event.pos())

        # Move scene to old position
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())


class MyGraphicsScene(QGraphicsScene):
    def __init__(self,  parent):
        super(MyGraphicsScene,  self).__init__()
        self.setBackgroundBrush(QBrush(QColor(50,50,50)))
        # self.setSceneRect(50,50,0,0)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setWindowTitle("Test")
        self.resize(800,600)

        self.gv = MyGraphicsView()
        self.gv.setScene(MyGraphicsScene(self))
        self.setCentralWidget(self.gv)

        self.gv.scene().selectionChanged.connect(self.selection_changed)
        self.populate()


    def populate(self):
        scene = self.gv.scene()

        for i in range(500):
            x = random.randint(0, 1000)
            y = random.randint(0, 1000)
            r = random.randint(2, 8)
            rect = scene.addEllipse(x, y, r, r, QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(255,128,20,128)))
            rect.setFlag( QGraphicsItem.ItemIsSelectable )
            rect.setFlag( QGraphicsItem.ItemIsMovable )

        rect = scene.addEllipse(300, 500, 20, 20, QPen(QColor(255,128,0), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin), QBrush(QColor(255,0,0,128)))
        rect.setFlag( QGraphicsItem.ItemIsSelectable )
        rect.setFlag( QGraphicsItem.ItemIsMovable )


    def selection_changed(self):
        selection = self.gv.scene().selectedItems()
        print('Selected:', len(selection))
        for i in selection:
            i.setPen(QPen(QColor(255,255,255), 0.5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))


def main():
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()