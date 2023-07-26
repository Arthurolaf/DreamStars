from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QTextEdit


class Window(QWidget):
    def __init__(self, name=None):
        QWidget.__init__(self)
        self.button_pressed = 1
        self.button = QPushButton('', self)

        self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon(r'C:\Users\Artur.Abaidulov\Projects\DreamStars\Images\arrow_down.png'))
        self.button.setIconSize(QtCore.QSize(20,20))
        self.button.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
        self.description = QPushButton(f'{name}', self)
        self.description.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")

        self.texted = QTextEdit()
        layout_tm = QVBoxLayout(self)

        layout = QHBoxLayout(self)
        
        layout.addWidget(self.description)
        layout.addWidget(self.button)

        layout_tm.addLayout(layout)
        layout_tm.addWidget(self.texted)

    def handleButton(self):
        if self.button_pressed == 0:
            self.button_pressed = 1
            self.button.setIcon(QtGui.QIcon(r'C:\Users\Artur.Abaidulov\Projects\DreamStars\Images\arrow_down.png'))
            self.button.setIconSize(QtCore.QSize(20,20))
            self.button.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
            self.texted.show()

        elif self.button_pressed == 1:
            self.button_pressed = 0
            self.button.setIcon(QtGui.QIcon(r'C:\Users\Artur.Abaidulov\Projects\DreamStars\Images\arrow_up.png'))
            self.button.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-right-color: white; border-bottom-color: white;}")
            self.button.setIconSize(QtCore.QSize(20,20))
            self.texted.hide()



# if __name__ == '__main__':

#     import sys
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())