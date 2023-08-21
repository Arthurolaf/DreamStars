import sys, random
from widget_panel_part import Mini_Widget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib.figure import Figure



class IndicSelectWindow(QDialog):

    def __init__(self, parent=None):
        super(IndicSelectWindow, self).__init__(parent=parent)
        self.resize(1000, 800)

        self.target = None
        self.setAcceptDrops(True)
        self.layout = QHBoxLayout(self)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)

        for i in range(3):
            for j in range(3):

                self.Frame = QFrame(self)
                self.Frame.setStyleSheet("background-color: white;")
                self.Frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
                self.Frame.setLineWidth(4)

                self.Frame2 = QFrame(self)
                self.Frame2.setFrameStyle(QFrame.Panel | QFrame.Raised)
                self.Frame2.setVisible(False)

                self.layout = QHBoxLayout(self.Frame)
                self.button = Mini_Widget(f'{i},{j}')

                if j <= 1 and i <= 1:
                    self.layout.addWidget(self.button)
                    self.layout.addWidget(self.button)
                    Box = QVBoxLayout()

                    Box.addWidget(self.Frame)

                    self.gridLayout.addLayout(Box, i, j)
                Box2 = QVBoxLayout()

                Box2.addWidget(self.Frame2)
                self.gridLayout.addLayout(Box2, i, j)
                self.gridLayout.setColumnStretch(i % 3, 1)
                self.gridLayout.setRowStretch(j, 1)

    def eventFilter(self, watched, event):
        if event.type() == QEvent.MouseButtonPress:
            self.mousePressEvent(event)
        elif event.type() == QEvent.MouseMove:
            self.mouseMoveEvent(event)
        elif event.type() == QEvent.MouseButtonRelease:
            self.mouseReleaseEvent(event)
        return super().eventFilter(watched, event)

    def get_index(self, pos):
        for i in range(self.gridLayout.count()):
            if self.gridLayout.itemAt(i).geometry().contains(pos) and i != self.target:
                return i

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:

            
            self.target = self.get_index(event.windowPos().toPoint())
        else:
            self.target = None

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton and self.target is not None:
            drag = QDrag(self.gridLayout.itemAt(self.target))
            pix = self.gridLayout.itemAt(self.target).itemAt(0).widget().grab()
            mimedata = QMimeData()
            mimedata.setImageData(pix)
            drag.setMimeData(mimedata)
            drag.setPixmap(pix)
            drag.setHotSpot(event.pos())
            drag.exec_()

    def mouseReleaseEvent(self, event):
        self.target = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if not event.source().geometry().contains(event.pos()):
            source = self.get_index(event.pos())
            if source is None:
                return

            i, j = max(self.target, source), min(self.target, source)
            p1, p2 = self.gridLayout.getItemPosition(i), self.gridLayout.getItemPosition(j)

            self.gridLayout.addItem(self.gridLayout.takeAt(i), *p2)
            self.gridLayout.addItem(self.gridLayout.takeAt(j), *p1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = IndicSelectWindow()
    w.show()
    sys.exit(app.exec_())