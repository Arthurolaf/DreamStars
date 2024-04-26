
import sys
import asyncio

from PyQt5 import QtCore, QtWidgets
from asyncqt import QEventLoop

from speedometr import Speedometer
from server import UDPserver


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.spd = Speedometer()
        self.spinBox = QtWidgets.QLineEdit()
        self.btn = QtWidgets.QPushButton("push")
        #self.e

        self.btn.clicked.connect(lambda value: self.btn_action())

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.spd)
        layout.addWidget(self.spinBox)
        layout.addWidget(self.btn)
    def btn_action(self):
        print(self.spinBox.text())
        print("button pressed")
        self.spd.setLabel(self.spinBox.text())
        #self.spinBox.text()

    @QtCore.pyqtSlot(float, float, float, float)
    def set_data(self, new_text,peer):
        print(peer)
        self.spd.setLabel(new_text)


async def create_server(loop):
    return await loop.create_datagram_endpoint(
        lambda: UDPserver(), local_addr=("127.0.0.1", 8889)
    )


def main():
    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    w = Widget()
    w.resize(640, 480)
    w.show()

    with loop:
        _, protocol = loop.run_until_complete(create_server(loop))
        protocol.dataChanged.connect(w.set_data)
        loop.run_forever()


if __name__ == "__main__":
    main()