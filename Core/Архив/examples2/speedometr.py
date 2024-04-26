from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt6.QtWidgets import QLabel
import time

class Speedometer(QtWidgets.QWidget):
    angleChanged = QtCore.pyqtSignal(float)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.lab = QtWidgets.QLabel()
        self.lab.setGeometry(20,20,20,20)
        self.lab.setText("teast")
        self.layt = QtWidgets.QHBoxLayout()
        self.layt.addWidget(self.lab)
        self.setLayout(self.layt)

        #self.setLabel(self.lab)
    def setLabel(self, text):
        print("asdlkfj")
        self.lab.setText(str(text))
        self.update()
        #time.sleep(10)


if __name__ == "__main__":
    import sys
    import asyncio
    from asyncqt import QEventLoop

    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    with loop:
        w = Speedometer()
        w.angle = 10
        w.show()
        loop.run_forever()