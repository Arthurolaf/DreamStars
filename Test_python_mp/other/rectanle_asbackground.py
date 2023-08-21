import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class GraphicsScene(QGraphicsScene):
    itemDoubleClicked = Signal(object)

class GraphicsRectangle(QGraphicsRectItem):
    def mouseDoubleClickEvent(self, event):
        self.scene().itemDoubleClicked.emit(self)

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.view = QGraphicsView()
        self.scene = GraphicsScene(self)
        self.view.setScene(self.scene)
        layout = QVBoxLayout(self)
        layout.addWidget(self.view)
        for i in range(1, 4):
            self.scene.addItem(GraphicsRectangle(50 * i, 50 * i, 20, 20))
        self.scene.itemDoubleClicked.connect(self.handleItemDoubleClicked)

    def handleItemDoubleClicked(self, item):
        print(item.boundingRect())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(600, 100, 300, 200)
    window.show()
    sys.exit(app.exec_())