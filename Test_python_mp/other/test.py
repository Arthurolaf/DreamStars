from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
class SceneObject(QGraphicsItem):
    def __init__(self, scene):
        QGraphicsItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIsSelectable, True)
        self.setFlag(QGraphicsItem.ItemHasNoContents, True)
        self.updateContents()

    def updateContents(self):
        self.prepareGeometryChange()
        for c in self.childItems():
            self.scene().removeItem(c)

        if self.isSelected():
            shape_item = QGraphicsRectItem()
        else:
            shape_item = QGraphicsEllipseItem()
        shape_item.setFlag(QGraphicsItem.ItemIsSelectable, False)
        shape_item.setFlag(QGraphicsItem.ItemStacksBehindParent,True)
        shape_item.setPen(QPen("green"))
        shape_item.setRect(QRectF(0,0,10,10))
        shape_item.setParentItem(self)

    def itemChange(self, change, value):
        if self.scene() != None:
            if change == QGraphicsItem.ItemSelectedHasChanged:
                self.updateContents()
                return
        return super(SceneObject,self).itemChange(change, value)

    def boundingRect(self):
        return self.childrenBoundingRect()


class Visualiser(QMainWindow):

    def __init__(self):
        super(Visualiser,self).__init__()

        self.viewer = QGraphicsView(self)
        self.viewer.setDragMode(QGraphicsView.RubberBandDrag)
        self.setCentralWidget(self.viewer)
        self.viewer.setScene(QGraphicsScene())

        parent_item = SceneObject(self.viewer.scene())
        parent_item.setPos(50,50)



app = QApplication([])
mainwindow = Visualiser()
mainwindow.show()
app.exec_()