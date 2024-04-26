from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
class start_menu(QWidget):
    def __init__(self, parent=None):
        """
        Класс является окном QWidget стартовым окном-меню игры, для выбора режима игры

        """
        super().__init__(parent)
        self.multplayer_state = False
        self._layout_ = QVBoxLayout(self)

        self._connecto_button = QPushButton("Connect")
        self._start_host_button = QPushButton("start host")

        self.single_game_btn = QPushButton("Single game")
        self.multiplayer_game_btn = QPushButton("Multiplayer game")
        self.multiplayer_game_btn.setVisible(False)

        self.load_single_btn = QPushButton("Load game.")
        self.load_single_btn.setVisible(False)

        self.load_multiplayer_btn = QPushButton("Load game...")
        self.load_multiplayer_btn.setVisible(False)

        self.new_game_single_btn = QPushButton("New game.")
        self.new_game_single_btn.setVisible(False)

        self.new_game_multiplayer_btn = QPushButton("New game...")
        self.new_game_multiplayer_btn.setVisible(False)

        self.connect_to_multiplayer_btn = QPushButton("Connect to host...")
        self.connect_to_multiplayer_btn.setVisible(False)

        self.back_main_btn = QPushButton("Back.")
        self.back_main_btn.setVisible(False)

        self._layout_.addWidget(self.single_game_btn)
        self._layout_.addWidget(self.multiplayer_game_btn)
        self._layout_.addWidget(self.new_game_single_btn)
        self._layout_.addWidget(self.new_game_multiplayer_btn)
        self._layout_.addWidget(self.load_single_btn)
        self._layout_.addWidget(self.load_multiplayer_btn)
        self._layout_.addWidget(self.connect_to_multiplayer_btn)
        self._layout_.addWidget(self.back_main_btn)


        self.single_game_btn.clicked.connect(lambda: self.start_btn_visible("down_singl"))
        self.multiplayer_game_btn.clicked.connect(lambda: self.start_btn_visible("down_multi"))
        self.back_main_btn.clicked.connect(lambda: self.start_btn_visible("up_main"))
        self.new_game_single_btn.clicked.connect(lambda: self.start_btn_visible("start_single"))

        self.load_multiplayer_btn.clicked.connect(lambda: self.start_btn_visible("load_multi"))
        self.connect_to_multiplayer_btn.clicked.connect(lambda: self.start_btn_visible("connect_multi"))

        self.setLayout(self._layout_)
        self.show()


############ Buttons menu action ##############
    def start_btn_visible(self, state: str):
        if state == "up_main":
            self.single_game_btn.setVisible(not self.multplayer_state)
            self.multiplayer_game_btn.setVisible(self.multplayer_state)
            self.load_single_btn.setVisible(False)
            self.load_multiplayer_btn.setVisible(False)
            self.back_main_btn.setVisible(False)
            self.new_game_single_btn.setVisible(False)
            self.new_game_multiplayer_btn.setVisible(False)
            self.connect_to_multiplayer_btn.setVisible(False)

        if state == "down_singl":
            self.new_game_single_btn.setVisible(True)
            self.single_game_btn.setVisible(False)
            self.multiplayer_game_btn.setVisible(False)
            self.load_single_btn.setVisible(True)
            self.back_main_btn.setVisible(True)
            #self.load_multiplayer_btn.setVisible(True)

        if state == "down_multi":
            self.new_game_multiplayer_btn.setVisible(True)
            self.single_game_btn.setVisible(False)
            self.multiplayer_game_btn.setVisible(False)
            self.load_multiplayer_btn.setVisible(True)
            self.back_main_btn.setVisible(True)
            self.connect_to_multiplayer_btn.setVisible(True)

        if state == "start_single":
            self.single_game_btn.setVisible(False)
            self.single_game_btn.setVisible(False)
            self.multiplayer_game_btn.setVisible(False)
            self.load_single_btn.setVisible(False)
            self.load_multiplayer_btn.setVisible(False)
            self.back_main_btn.setVisible(False)
            self.new_game_single_btn.setVisible(False)
            self.new_game_multiplayer_btn.setVisible(False)

        if state == "start_multi":
            self.multplayer_server_set()
        if state == "connect_multi":
            self.multplayer_server_set("connect")

    def multplayer_server_set(self,status="start"):
        for i in reversed(range(self._layout_.count())):
            self._layout_.itemAt(i).widget().deleteLater()

        client_layout = QGridLayout()
        if status == "start":
            self.loby_label = QLabel("Players number:")
            self._loby_line_edit = QLineEdit("3")

            self.loby_label.setBuddy(self._loby_line_edit)
            self._loby_line_edit.textChanged.connect(self.enable_get_fortune_button)
            client_layout.addWidget(self.loby_label, 3, 0)
            client_layout.addWidget(self._loby_line_edit, 3, 1)
            client_layout.addWidget(self._start_host_button, 4, 1)
        elif status == "connect":
            client_layout.addWidget(self._connecto_button, 4, 1)

        #client_layout.addWidget(self.host_label, 0, 0)
        #client_layout.addWidget(self._host_line_edit, 0, 1)
        #client_layout.addWidget(self.port_label, 1, 0)
        #client_layout.addWidget(self._port_line_edit, 1, 1)
        #client_layout.addWidget(self.user_label, 2, 0)
        #client_layout.addWidget(self._user_line_edit, 2, 1)



        self._layout_.addLayout(client_layout)
        self.update()
    # def enable_get_fortune_button(self):
    #     try:
    #         self._connecto_button.setEnabled(bool(self._host_line_edit.text() and
    #                                           self._port_line_edit.text() and self._user_line_edit.text()))
    #     except:
    #         self._start_host_button.setEnabled(bool(self._host_line_edit.text() and
    #                                           self._port_line_edit.text() and self._user_line_edit.text()))