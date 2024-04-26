from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
class host_room(QWidget):
    def __init__(self, parent=None,host_name=None,lobby_size=0):
        """
        Класс является окном QWidget отображающиее подключение новых игроков к Лобби

        Добавление происходит через функцию player_connect()
        Принудительное удаление игроков выполняет функция kick_player()

        """
        super().__init__(parent)
        self._layout_ = QVBoxLayout()
        self.player_maximum = lobby_size
        self.player_connected = 0
        self.connected_lines = QGridLayout()
        self.players = {}
        self.players_stat = {}
        #self.player_connect()

        self.host_name_label = QLabel(f"Host Player Name:{host_name}")
        self.players_counted_label = QLabel(f"connected/maximum")
        self.players_counted_status_label = QLabel(f"{self.player_connected}/{self.player_maximum}")

        self._ready_to_start_button = QCheckBox("Ready")
        self._start_button = QPushButton("Start")
        self._start_button.setDefault(True)

        self.client_layout = QGridLayout()
        self.client_layout.addWidget(self.host_name_label, 0, 0)
        self.client_layout.addWidget(self.players_counted_label, 1, 0)
        self.client_layout.addWidget(self.players_counted_status_label, 2, 0)

        self.client_layout.addWidget(self._start_button, 3, 1)
        self.client_layout.addWidget(self._ready_to_start_button,3,0)
        #self.player_connect(host_name,"hosted")
        self._layout_.addLayout(self.client_layout)
        self._layout_.addLayout(self.connected_lines)
        #self._start_button.clicked.connect()
        self.setLayout(self._layout_)


    def player_connect(self, player_list=None):
        """
        Добавляет пользователя в лобби
        Если был передан словарь {name, status}
        задает количестов заданных место, исходя из количества переданных имен
        """
        print(player_list, "--- Player_list geted")


        if player_list is not None:
            self.player_connected = len(player_list.keys())
            for x in reversed(range(self.connected_lines.count())):
                self.connected_lines.itemAt(x).widget().deleteLater()

            pl = list(player_list.keys())
            for player_num in range(0,len(pl)):

                self.players[player_num] = pl[player_num]
                self.players_stat[player_num] = player_list[pl[player_num]]
                if self.player_connected <= int(self.player_maximum):
                    print(f"{self.player_connected}/{self.player_maximum}")
                    self.players_counted_status_label.setText(f"{self.player_connected}/{self.player_maximum}")



            for i in range(0,len(player_list.keys())):
                print(f"Line seted: {i}",f"connected counter: {self.player_connected}",f" | plr conuted: {len(player_list.keys())}")
                self._player_status = QLabel(self.players_stat[i])
                self._player_line = QLineEdit(self.players[i])
                if self.players_stat[i] == "hosted":
                    self.host_name_label.setText(f"Host Player Name:{self.players[i]}")
                #self.players_counted_status_label.setText(f"{self.player_connected}/{self.player_maximum}")
                self._player_line.setEnabled(False)
                self.connected_lines.addWidget(self._player_line, i,0)
                self.connected_lines.addWidget(self._player_status, i, 1)
                #self._layout_.addLayout(self.connected_lines)
                self._layout_.update()
            self.update()

    def kick_player(self):
        pass