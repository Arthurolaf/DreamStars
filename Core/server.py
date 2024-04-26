# Copyright (C) 2013 Riverbank Computing Limited.
# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

"""PySide6 port of the network/fortuneserver example from Qt v5.x"""

import random
import sys

from PySide6.QtCore import QByteArray, QDataStream, QIODevice, Qt,QTimer
from PySide6.QtNetwork import QTcpServer,QHostAddress
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout,
                               QLabel, QMessageBox, QPushButton,
                               QVBoxLayout,QWidget)
import json

class Server(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.game_lobby_size = ""
        self.map_size = ""
        self.player_list = {}
        self.client_turn = 0
        self.server_turn = 0
        self.chat_player_name = ""
        self.chat_message = ""
        self.client_map_ = {}
        self.server_map_ = {}
        self.turn_check = {}

        self.port = 2000
        self.host = "127.0.0.1"
        self.connected = {}
        self.loby_long = None
        self.player_in_loby = 0
        status_label = QLabel()
        status_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        quit_button = QPushButton("Quit")
        quit_button.setAutoDefault(False)
        self._timer = QTimer(self, interval=5000)
        self._timer.start()
        self._tcp_server = QTcpServer(self)
        self._timer.timeout.connect(lambda : self.conected_check())

        if not self._tcp_server.listen(QHostAddress(self.host),self.port):
            reason = self._tcp_server.errorString()
            QMessageBox.critical(self, "Fortune Server",
                    f"Unable to start the server: {reason}.")
            self.close()
            return
        self._tcp_server.newConnection.connect(self.on_newConnection)

        port = self._tcp_server.serverPort()
        status_label.setText(f"The server is running on port {port}.\nRun the "
                "Fortune Client example now.")

        self.fortunes = (
                "You've been leading a dog's life. Stay off the furniture.",
                "Computers are not intelligent. They only think they are.")

        quit_button.clicked.connect(self.close)
        #self._tcp_server.newConnection.connect(self.send_fortune)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(quit_button)
        button_layout.addStretch(1)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(status_label)
        main_layout.addLayout(button_layout)


        self.setWindowTitle("Fortune Server")
    ################## New Method ###############
    def msg_builder(self):
        """
        """
        msg = {
            2: {"game_lobby_size": self.game_lobby_size, "map_size": self.map_size, "player_list": self.player_list},
            3: {"server_turn": self.server_turn, "client_turn": self.client_turn,
                "chat_player_name": self.chat_player_name, "chat_message": self.chat_message},
            4: {"server_map_": self.server_map_, "client_map_": self.client_map_}
        }

        return str(msg)

    def msg_parser(self, msg):
        """
        """
        # print(eval(msg))

        self.first_line(eval(msg)[1])
        self.second_line(eval(msg)[2], eval(msg)[1])
        self.third_line(eval(msg)[3], eval(msg)[1])
        self.fourth_line(eval(msg)[4], eval(msg)[1])
        self.send_fortune()
        pass

    def first_line(self, data):
        if ("hosted" not in self.player_list.values() or self.player_list == {}) and data["game_status"] == "hosted":
            self.player_list[data["player_name"]] = data["game_status"]
            self.connected[data["player_name"]] = 1
        elif "hosted" in self.player_list.values() and data["game_status"] != "hosted":
            self.player_list[data["player_name"]] = data["game_status"]
            self.connected[data["player_name"]] = 1
        elif data["player_name"] in self.player_list and self.player_list[data["player_name"]] == "hosted":
                self.connected[data["player_name"]] = 1

        # print(self.player_list)

    def second_line(self, data, pdata):
            if pdata["game_status"] == "hosted":
                self.game_lobby_size = data["game_lobby_size"]
                self.map_size = data["map_size"]


    def third_line(self, data, pdata):
        self.server_turn = 0
        self.turn_check[pdata["player_name"]] = data["client_turn"]
        self.chat_player_name = data["chat_player_name"]
        self.chat_message = data["chat_message"]
        pass

    def fourth_line(self, data, pdata):
        self.client_map_ = {pdata["player_name"]: data["client_map_"]}
        self.server_map_ = {pdata["player_name"]: "map_data"}
        pass

    def create_loby(self, loby_long):
        print(self.loby_long, "self.loby_long creation" )
        if self.loby_long is None:
            self.loby_long = int(loby_long)
        else:
            pass
    def check_loby_full(self):
        if self.game_lobby_size != "":
            self.player_in_loby = (len(self.player_list.keys()))
            try:
                if self.loby_long == self.player_in_loby:
                    return True
                else:
                    return False
            except:
                return False
        return False
    def conected_check(self):
        if self.connected == {}:
            print("self.connected is empty")
        else:
            print(self.connected)
            for keys, values in self.connected.items():
                print(keys, "-- now",values)
                try:
                    self.connected[keys] += 5
                except KeyError:
                    break
                if values >= 15 and values < 30:
                    print("//////",self.player_list[keys],self.connected[keys])
                    print(keys,"was desconnected")
                    self.player_list[keys] = "desconnected"
                    #del self.connected[keys]
                elif values >= 30:
                    print(keys,"leave lobby desconnected")
                    del self.player_list[keys]
                    del self.connected[keys]




    def send_fortune(self):
        self.block = QByteArray()
        out = QDataStream(self.block, QIODevice.WriteOnly)
        out.setVersion(QDataStream.Qt_4_0)
        out.writeUInt16(0)
        fortune = self.msg_builder()

        out.writeString(fortune)
        out.device().seek(0)
        out.writeUInt16(self.block.size() - 2)

    def on_newConnection(self):
        self.client_connection = self._tcp_server.nextPendingConnection()
        self.client_connection.disconnected.connect(self.client_connection.deleteLater)

        self.client_connection.readyRead.connect(self.on_readyRead)


    def on_readyRead(self):
        self.client_connection = self.sender()
        instr = QDataStream(self.client_connection)
        instr.setVersion(QDataStream.Qt_4_0)

        self._block_size = instr.readUInt16()
        message = instr.readString()

        self.msg_parser(message)

        if self._block_size == 0:
            return
        if message == '':
            return


        self._current_message = message
        #print(self._current_message)

        self.client_connection.write(self.block)

        self.client_connection.disconnectFromHost()


def main():
    app = QApplication(sys.argv)
    random.seed(None)
    server = Server()

    server.show()
    sys.exit(app.exec())

if __name__ == '__main__':
   main()
