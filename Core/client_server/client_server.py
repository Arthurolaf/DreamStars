
import sys
import random
from PySide6.QtCore import QDataStream, QTimer, QByteArray, QIODevice,Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtNetwork import QAbstractSocket, QTcpSocket,QTcpServer,QHostAddress
from PySide6.QtWidgets import (QApplication, QDialog, QDialogButtonBox, QGridLayout, QHBoxLayout, QVBoxLayout,
                               QLabel, QLineEdit, QMessageBox, QPushButton)
import json


class Server_client(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.port = 2000
        # описание статуса сервера
        status_label = QLabel()
        # Определяет как отображать текст
        status_label.setTextInteractionFlags(Qt.TextBrowserInteraction)

        #Задаем кнопку выхоа
        quit_button = QPushButton("Quit")
        quit_button.setAutoDefault(False)

        #задаем объект сервера что запустить сервер с указанием порта и ip на котором слушать
        # host = 127.0.0.1 ; port = 9999
        # проверяем если сервер не запущен выводим ошибку по которой он не запущен
        # а так же сообщаем пользователю, что не смогли запустить сервер на указаном порту

        self._tcp_server = QTcpServer(self)
        if not self._tcp_server.listen(QHostAddress("127.0.0.1"),self.port):
            reason = self._tcp_server.errorString()
            QMessageBox.critical(self, "Fortune Server",
                    f"Unable to start the server: {reason}.")
            self.close()
            return

        # По умолчанию были другие настройки и порт брался случайно,
        # поэтому данная коммманда спрашивает какой порт прослушиватеся
        port = self._tcp_server.serverPort()
        # Выводим на диалоговом окне сообщение о состоянии сервера
        status_label.setText(f"The server is running on port {port}.\nRun the "
                "Fortune Client example now.")

        # Переменная в которой задается список ответов для клиента
        self.fortunes = (
                "You've been leading a dog's life. Stay off the furniture.",
                "You've got to think about tomorrow.",
                "You will be surprised by a loud noise.",
                "You will feel hungry again in another hour.",
                "You might have mail.",
                "You cannot kill time without injuring eternity.",
                "Computers are not intelligent. They only think they are.")

        # Задаем кнопке выхода действие (закрыть приложение)
        quit_button.clicked.connect(self.close)
        # Что делать с новым подключении к серверу задается в функции (send_forutne)
        self._tcp_server.newConnection.connect(self.send_fortune)





        #self.setWindowTitle("Fortune Server")

        ####Cleint ###

        self._block_size = 0
        self._current_fortune = ''

        host_label = QLabel("Server name:")
        port_label = QLabel("Server port:")
        msg_label = QLabel("Sending msg:")

        self._host_line_edit = QLineEdit('Localhost')
        self._port_line_edit = QLineEdit()
        self._msg_line_edit = QLineEdit()
        self._port_line_edit.setValidator(QIntValidator(2000, 2023, self))

        host_label.setBuddy(self._host_line_edit)
        port_label.setBuddy(self._port_line_edit)
        msg_label.setBuddy(self._msg_line_edit)

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
        self._msg_line_edit.textChanged.connect(self.enable_get_fortune_button)
        self._get_fortune_button.clicked.connect(self.request_new_fortune)
        quit_button.clicked.connect(self.close)
        self._tcp_socket.readyRead.connect(self.read_fortune)
        self._tcp_socket.errorOccurred.connect(self.display_error)

        # Тут интерфейс ни чего сложного
        #button_layout = QHBoxLayout()
        #button_layout.addStretch(1)
        #button_layout.addWidget(quit_button)
        #button_layout.addStretch(1)
        #
        client_layout = QGridLayout()
        #
        client_layout.addWidget(host_label, 0, 0)
        client_layout.addWidget(self._host_line_edit, 0, 1)
        client_layout.addWidget(port_label, 1, 0)
        client_layout.addWidget(self._port_line_edit, 1, 1)
        client_layout.addWidget(msg_label, 2, 0)
        client_layout.addWidget(self._msg_line_edit, 2, 1)
        client_layout.addWidget(self._status_label, 3, 0, 1, 2)
        client_layout.addWidget(button_box, 4, 0, 1, 2)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(status_label)
        main_layout.addLayout(client_layout)
        #main_layout.addLayout(button_layout)

        self.setWindowTitle("Fortune Client")
        self._port_line_edit.setFocus()


    def send_fortune(self):
        """
        функция задает параметры для сообщение которое будет отправлено новому подключению
        И отправляет рандомную строку из списка ответов
        """
        # задаем блок данных который будем заполнять
        block = QByteArray()

        # заполняем блок
        out = QDataStream(block, QIODevice.WriteOnly)
        out.setVersion(QDataStream.Qt_4_0)
        # номер строки
        out.writeUInt16(0)
        # берем рандомное значение из вариантов
        fortune = self._msg_line_edit.text()#self.fortunes[random.randint(0, len(self.fortunes) - 1)]
        # передаем как строку в блок
        out.writeString(fortune)

        out.device().seek(0)
#        out.writeUInt16(block.size() - 2)

        client_connection = self._tcp_server.nextPendingConnection()
        client_connection.disconnected.connect(client_connection.deleteLater)

        client_connection.write(block)
        client_connection.disconnectFromHost()

# class Client(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)



    def request_new_fortune(self):
        self._get_fortune_button.setEnabled(False)
        self._block_size = 0
        self._tcp_socket.abort()
        self._tcp_socket.connectToHost(self._host_line_edit.text(),
                int(self._port_line_edit.text()))

    def read_fortune(self):
        instr = QDataStream(self._tcp_socket)
        instr.setVersion(QDataStream.Qt_4_0)

        if self._block_size == 0:
            if self._tcp_socket.bytesAvailable() < 2:
                return

            self._block_size = instr.readUInt16()

        if self._tcp_socket.bytesAvailable() < self._block_size:
            return

        next_fortune = instr.readString()
        # try:
        #     settings = json.load(next_fortune)
        #     print()
        #     if settings["port"] is not None or settings["port"] != 2000:
        #         self.port = settings["port"]
        #         self._tcp_server.listen(QHostAddress("127.0.0.1"),self.port)
        # except :
        #     print(next_fortune)
        #     pass
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
    server = Server_client()
    random.seed(None)
    sys.exit(server.exec())
