from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QTextEdit,QFrame



class Mini_Widget(QWidget):
    def __init__(self, name=None):
        QFrame.__init__(self)
        self.setStyleSheet("""QFramewidget_panel_part.py{
                                border: 3px dashed #aaa
                                } """)
        self.button_pressed = 1
        self.button = QPushButton('', self)

        self.button.setFixedSize(25,25)

        #self.button.clicked.connect(self.handleButton)
        self.button.setIcon(QtGui.QIcon(r'../../Images/arrow_down.png'))
        self.button.setIconSize(QtCore.QSize(20,20))
        self.button.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
        #self.description = QPushButton(f'{name}', self)

        #self.description.setFixedHeight(25)

        #self.description.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
        #self.description.cli
        self.texted = QTextEdit()



        self.layout_tm = QVBoxLayout(self)

        self.layout_m = QHBoxLayout(self)

        #layout.addWidget(self.description)
        self.layout_m.addWidget(self.button)

        self.layout_tm.addLayout(self.layout_m)
        self.layout_tm.addWidget(self.texted)

    def handleButton(self):

        if self.button_pressed == 0:
            self.button_pressed = 1
            self.button.setIcon(QtGui.QIcon(r'../../Images/arrow_down.png'))
            self.button.setIconSize(QtCore.QSize(20,20))
            self.button.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-left-color: white; border-top-color: white;}")
            self.texted.show()

        elif self.button_pressed == 1:
            self.button_pressed = 0
            self.button.setIcon(QtGui.QIcon(r'../../Images/arrow_up.png'))
            self.button.setStyleSheet("QPushButton {border-style: solid; border-width: 2px; border-right-color: white; border-bottom-color: white;}")
            self.button.setIconSize(QtCore.QSize(20,20))
            self.texted.hide()

    def widget_pressed(self):
        print('rar')
        return 1

# if __name__ == '__main__':

#     import sys
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())