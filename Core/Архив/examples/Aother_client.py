# Copyright (C) 2013 Riverbank Computing Limited.
# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the network/fortuneclient example from Qt v5.x"""

import sys

from PySide6.QtCore import QDataStream, QTimer
from PySide6.QtGui import QIntValidator
from PySide6.QtNetwork import QAbstractSocket, QTcpSocket
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QGridLayout,
                               QLabel, QLineEdit, QMessageBox, QPushButton)


class Client(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._block_size = 0
        self._current_fortune = ''

        host_label = QLabel("&Server name:")
        port_label = QLabel("S&erver port:")

        self._host_line_edit = QLineEdit('Localhost')
        self._port_line_edit = QLineEdit()
        self._port_line_edit.setValidator(QIntValidator(1, 65535, self))

        host_label.setBuddy(self._host_line_edit)
        port_label.setBuddy(self._port_line_edit)

        self._status_label = QLabel("This examples requires that you run "
                "the Fortune Server example as well.")

        self._get_fortune_button = QPushButton("Get Fortune")
        self._get_fortune_button.setDefault(True)
        self._get_fortune_button.setEnabled(False)

        quit_button = QPushButton("Quit")

        button_box = QDialogButtonBox()
        button_box.addButton(self._get_fortune_button,
                QDialogButtonBox.ActionRole)
        button_box.addButton(quit_button, QDialogButtonBox.RejectRole)

        self._tcp_socket = QTcpSocket(self)

        self._host_line_edit.textChanged.connect(self.enable_get_fortune_button)
        self._port_line_edit.textChanged.connect(self.enable_get_fortune_button)
        self._get_fortune_button.clicked.connect(self.request_new_fortune)
        quit_button.clicked.connect(self.close)
        self._tcp_socket.readyRead.connect(self.read_fortune)
        self._tcp_socket.errorOccurred.connect(self.display_error)

        main_layout = QGridLayout(self)
        main_layout.addWidget(host_label, 0, 0)
        main_layout.addWidget(self._host_line_edit, 0, 1)
        main_layout.addWidget(port_label, 1, 0)
        main_layout.addWidget(self._port_line_edit, 1, 1)
        main_layout.addWidget(self._status_label, 2, 0, 1, 2)
        main_layout.addWidget(button_box, 3, 0, 1, 2)

        self.setWindowTitle("Fortune Client")
        self._port_line_edit.setFocus()

    def request_new_fortune(self):
        self._get_fortune_button.setEnabled(False)
        print(self._block_size, "test")
        self._block_size = 0
        self._tcp_socket.abort()
        self._tcp_socket.connectToHost(self._host_line_edit.text(),
                int(self._port_line_edit.text()))

    def read_fortune(self):
        instr = QDataStream(self._tcp_socket)
        infort = QDataStream(self._tcp_socket)
        instr.setVersion(QDataStream.Qt_4_0)
        self._block_size = instr.readUInt16()
        print(instr.readString())
        print(self._block_size)
        if self._block_size == 0:
            if self._tcp_socket.bytesAvailable() < 2:
                return

            self._block_size = instr.readUInt16()
            print(self._block_size)
        if self._tcp_socket.bytesAvailable() < self._block_size:
            return

        next_fortune = instr.readString()

        if next_fortune == self._current_fortune:
            QTimer.singleShot(0, self.request_new_fortune)
            return

        self._current_fortune = next_fortune
        self._status_label.setText(self._current_fortune)
        self._get_fortune_button.setEnabled(True)

    def display_error(self, socketError):
        if socketError == QAbstractSocket.RemoteHostClosedError:
            pass
        elif socketError == QAbstractSocket.HostNotFoundError:
            QMessageBox.information(self, "Fortune Client",
                    "The host was not found. Please check the host name and "
                    "port settings.")
        elif socketError == QAbstractSocket.ConnectionRefusedError:
            QMessageBox.information(self, "Fortune Client",
                    "The connection was refused by the peer. Make sure the "
                    "fortune server is running, and check that the host name "
                    "and port settings are correct.")
        else:
            reason = self._tcp_socket.errorString()
            QMessageBox.information(self, "Fortune Client",
                    f"The following error occurred: {reason}.")

        self._get_fortune_button.setEnabled(True)

    def enable_get_fortune_button(self):
        self._get_fortune_button.setEnabled(bool(self._host_line_edit.text() and
                self._port_line_edit.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = Client()
    client.show()
    sys.exit(client.exec())