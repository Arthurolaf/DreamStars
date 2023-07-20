from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class GraphicView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)       
        self.setSceneRect(0, 0, 300, 300)
        #self.setGeometry(0, 0, 200, 200)
        #self.moveObject = MovingObject(50, 50, 40)
        #self.moveObject2 = MovingObject(100, 100, 100)
        #self.scene.addItem(self.moveObject)
        #self.scene.addItem(self.moveObject2)
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainApp(QMainWindow):
    """This is the class of the MainApp GUI system"""
    def __init__(self):
        """Constructor method that inherits methods from QWidgets"""
        super().__init__()
        self.initUI()

    def initUI(self):
        """This method creates our GUI"""
        
        centralwidget = QWidget()
        self.setCentralWidget(centralwidget)
        MainGrid = QGridLayout(centralwidget)
        #vertical = QVBoxLayout(centralwidget)
        #horizontal = QHBoxLayout(centralwidget)
        
        # Box Layout to organize our GUI
        # labels
        MainGrid.addWidget(Color('black'), 0, 1)
        types1 = QLabel('try it')
        model = GraphicView()
        MainGrid.addWidget(types1)
        #lay.addWidget(model)


        frame = QFrame(model)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("QWidget { background-color: gray }")
        frame.setGeometry(50, 50, 100, 100)
        
        self.setGeometry(0, 0, 900, 900)
        self.setFixedSize(self.size())
        self.setWindowTitle('MainApp')
        self.setWindowIcon(QIcon('image/logo.png'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainApp()
    sys.exit(app.exec_())