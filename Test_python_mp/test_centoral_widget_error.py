
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

class MainApp(QMainWindow):
    """This is the class of the MainApp GUI system"""
    def __init__(self):
        """Constructor method"""
        super().__init__()
        self.initUI()

    def initUI(self):
        """This method creates our GUI"""

        # Box Layout to organize our GUI
        # labels
        types1 = QLabel('Label', self)
        types1.resize(170, 20)
        types1.move(1470, 580)

        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)

        self.tree.setWindowTitle("Directory Viewer")
        self.tree.resize(323, 300)
        self.tree.show()

        self.setGeometry(50, 50, 1800, 950)
        self.setFixedSize(self.size())
        self.centering()
        self.setWindowTitle('MainApp')
        self.setWindowIcon(QIcon('image/logo.png'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainApp()
    w.show()
    sys.exit(app.exec_())
    self.show()