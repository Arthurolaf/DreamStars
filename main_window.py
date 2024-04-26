import sys

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtNetwork import QAbstractSocket, QTcpSocket,QHostAddress
from GUI.main.Hidenbutton import changeVisibility
from GUI.main.map import  main_map_scen,MyView
from GUI.main.control_panel import  Top_left_window
from GUI.host_connect_room import host_room
from GUI.first_start_menu import start_menu

import json

class Main_Window(QWidget):
    def __init__(self, load_game=None, username="anonymous"):
        super(Main_Window, self).__init__()
        self.process_counter = 1
        self.load_game = load_game
        self.username = username
        self.initUI()
        self.p = None
        self.text = QPlainTextEdit()
        self.message_to_send = ""
        self.error_counter = 0
        self.loby_size = 1
        self.multiplaer = False
        self.server = None
        ###
        #self.username = "John"
        self.game_status = "connected"
        self.player_id = "91958ZDk"
        self.game_lobby_size = "1"
        self.map_size = ""
        self.player_list = {}
        self.client_turn = 0
        self.server_turn = 0
        self.chat_player_name = ""
        self.chat_message = ""
        self.client_map_ = {}
        self.server_map_ = {}
        self.host_name = ""


    def initUI(self):


        self.main_layout_box = QVBoxLayout(self)
        # temporary placeholder
        bottom_left = QFrame(self)
        self.test_btn = QPushButton("Test")
        self.test_btn.setDisabled(True)
        test_save_btn = QPushButton("Save")
        test_load_btn = QPushButton("load")

        self.fild = QLineEdit(self)
        test_lut = QHBoxLayout(bottom_left)
        test_lut.addWidget(test_save_btn)
        test_lut.addWidget(test_load_btn)
        test_lut.addWidget(self.test_btn)
        test_lut.addWidget(self.fild)

        bottom_left.setFrameShape(QFrame.StyledPanel)
        top_left = Top_left_window()
        top_left2 = QFrame(self)
        # Control_panel




        # This area should contain the "Objects control panel" and the Map. Lets add it.

        splitter_ocp_nd_map = QSplitter(Qt.Horizontal) # The splitter moves along the horizontal (but the splitter itself is vertical)

        # Add Objects control panel (control_panel)
        splitter_ocp_nd_map.addWidget(top_left)


        if self.load_game is not None:
            self.map = main_map_scen(load_game=self.load_game)
        else:
            self.map = main_map_scen()

        test_save_btn.clicked.connect(self.test_btn.setDisabled(False))

        self.status_bar_map = QVBoxLayout()
        self.online_status = QHBoxLayout()

        self.s_p1 = QLabel(self)

        self.s_p1.resize(10,10)
        self.s_p1.setStyleSheet("background-color : orange")
        self.s_p2 = QLabel(self)

        self.s_p2.resize(10, 10)
        self.s_p2.setStyleSheet("background-color : orange")
        self.s_p3 = QLabel(self)

        self.s_p3.resize(10, 10)
        self.s_p3.setStyleSheet("background-color : orange")

        self.s_p4 = QLabel(self)

        self.s_p4.resize(10, 10)
        self.s_p4.setStyleSheet("background-color : orange")
        self.s_p5 = QLabel(self)

        self.s_p5.resize(10, 10)
        self.s_p5.setStyleSheet("background-color : orange")
        self.s_p6 = QLabel(self)

        self.s_p6.resize(10, 10)
        self.s_p6.setStyleSheet("background-color : orange")
        self.online_status.addWidget(self.s_p4)
        self.online_status.addWidget(self.s_p5)
        self.online_status.addWidget(self.s_p6)

        self.online_status.addWidget(self.s_p1)
        self.online_status.addWidget(self.s_p2)
        self.online_status.addWidget(self.s_p3)

        self.status_bar_map.addLayout(self.online_status)

        splitter_ocp_nd_map.addWidget(self.map.model) # Place the map in the splitter area

        splitter_ocp_nd_map.setSizes([200,200])


        # This area should contain event messages and additional object descriptions.
        splitter_msgs_nd_dscr = QSplitter(Qt.Horizontal)
        splitter_msgs_nd_dscr.addWidget(bottom_left)
        splitter_msgs_nd_dscr.addWidget(changeVisibility())

        self.splitter2 = QSplitter(Qt.Vertical)
        self.splitter2.setMaximumWidth(2000)
        self.splitter2.addWidget(splitter_ocp_nd_map)
        self.splitter2.addWidget(splitter_msgs_nd_dscr)


        ############# Start menu buttons
        self.strt = start_menu()
        self.strt.setVisible(False)
        self.strt.new_game_multiplayer_btn.clicked.connect(lambda : self.set_hosted_state())
        self.strt.connect_to_multiplayer_btn.clicked.connect(lambda :self.connect_lobby_room())
        #self.strt._start_host_button.clicked.connect(self.create_connection)
        self.user_label = QLabel("User name:")
        self._user_line_edit = QLineEdit()
        self._enter_name = QPushButton("Enter")
        self.layout_enter_name = QGridLayout()
        self.multiplayer_check_box = QCheckBox("Multiplayer (if host fild default you will by server)")
        self.host_label = QLabel("Server name:")
        self.port_label = QLabel("Server port:")
        #self.mp_host = QLabel("Players set if you are server-host")
        self.layout_mp_host = QHBoxLayout()
        #self.mp_host.setStyleSheet("* { color: gray }")
        self.lobby_setter_group = QGroupBox("set if you are server-host:")
        self.lobby_setter_group.setLayout(self.layout_mp_host)

        self.plrs_in_lobby = QLabel("Player in game:")
        self.layout_mp_host.addWidget(self.plrs_in_lobby)
        #self.plrs_in_lobby.setStyleSheet("* { color: gray }")


        self._host_line_edit = QLineEdit('127.0.0.1')
        self._host_line_edit.setDisabled(True)
        self._port_line_edit = QLineEdit("2000")
        self._port_line_edit.setDisabled(True)
        self._loby_line_edit = QLineEdit("1")
        self._loby_line_edit.setDisabled(True)


        self.host_label.setBuddy(self._host_line_edit)
        self.port_label.setBuddy(self._port_line_edit)
        self.user_label.setBuddy(self._user_line_edit)

#        self.lobby_setter_group.setVisible(False)

        self._enter_name.clicked.connect(lambda : self.vis_start_menu())
        self.multiplayer_check_box.toggled.connect(self._host_line_edit.setEnabled)
        self.multiplayer_check_box.toggled.connect(self._port_line_edit.setEnabled)
        self.multiplayer_check_box.toggled.connect(self.multiplaer_set)
        #self.multiplayer_check_box.toggled.connect(self.plrs_in_lobby.setEnabled)
        self.multiplayer_check_box.toggled.connect(self._loby_line_edit.setEnabled)

        self.multiplayer_check_box.toggled.connect(self.lobby_setter_group.setEnabled)


        self.layout_enter_name.addWidget(self.user_label,0,0)
        self.layout_enter_name.addWidget(self._user_line_edit,0,1)
        self.layout_enter_name.addWidget(self._enter_name,6,0)
        self.layout_enter_name.addWidget(self.multiplayer_check_box,1,0)
        self.layout_enter_name.addWidget(self.host_label, 2, 0)
        self.layout_enter_name.addWidget(self.port_label, 3, 0)
        self.layout_enter_name.addWidget(self._host_line_edit,2,1)
        self.layout_enter_name.addWidget(self._port_line_edit,3,1)

#        self.layout_enter_name.addWidget(self.mp_host,4,0)
        self.layout_enter_name.addWidget(self.lobby_setter_group,5,0)
        self.layout_enter_name.addWidget(self._loby_line_edit, 5, 1)

        self.main_layout_box.addLayout(self.layout_enter_name)
        self.main_layout_box.addWidget(self.strt)
        self.strt.new_game_multiplayer_btn.clicked.connect(lambda: self.create_lobby_room())

        self.main_layout_box.addWidget(self.splitter2)
        self.main_layout_box.addLayout(self.status_bar_map)

        self.setLayout(self.main_layout_box)

        player = self.username
        self.setGeometry(0, 900, 900, 900)
        self.setWindowTitle(f'Dream Stars {player}')

        self.test_btn.clicked.connect(lambda : self.request_new_fortune())
        self.map.model.itemDoubleClicked.connect(self.handleItemDoubleClicked)
        self.map.model.itemSelect.connect(self.item_selected)
        self.map.model.itemAddWay.connect(self.drow_path)
        test_load_btn.clicked.connect(lambda : self.map_gen())
        self.splitter2.setVisible(False)
        self.s_p6.setVisible(False)
        self.s_p5.setVisible(False)
        self.s_p4.setVisible(False)
        self.s_p3.setVisible(False)
        self.s_p2.setVisible(False)
        self.s_p1.setVisible(False)

        self.show()


############ Buttons menu action ##############

    def set_hosted_state(self):
        self.game_status = "hosted"
        self.create_connection()
    def create_lobby_room(self):

        self.room = host_room(host_name=self.username, lobby_size=self.loby_size)
        #self.message_to_send = self.msg_builder()
        #self.request_new_fortune()
        self.strt.setVisible(False)
        #self.message_to_send = self.msg_builder()
        self.main_layout_box.addWidget(self.room)
        #self.multiplayer_check_box.toggled.connect(self._loby_line_edit.setEnabled)
        self.room._ready_to_start_button.toggled.connect(self.set_ready)
        self.lobby_timer = QTimer(self, interval=2000)
        self.lobby_timer.start()
        self.lobby_timer.timeout.connect(self.player_connect_lobby)
    def connect_lobby_room(self):
            #print(f"Uhaha -- {self.player_list}, {self.game_lobby_size}")
            self.room = host_room(host_name=self.username, lobby_size=self.game_lobby_size)
            self.strt.setVisible(False)
            self.main_layout_box.addWidget(self.room)
            self.room._ready_to_start_button.toggled.connect(self.set_ready)
            self.lobby_timer = QTimer(self, interval=2000)
            self.lobby_timer.start()
            self.lobby_timer.timeout.connect(self.player_connect_lobby)
            self.create_connection()
            self.room.player_maximum = self.game_lobby_size
    def player_connect_lobby(self):

        if self.player_list != {}:
            print("----", self.player_list)
            self.room.player_connect(self.player_list)

            self.room.update()
            #for name in self.player_list.keys():
                #self.room.player_connect(name,self.player_list[name])
    def lobby_status(self):
        self.room.player_maximum = self.game_lobby_size
        self.room.player_connected = len(self.player_list)
        self.room.update()
    def set_ready(self,state):

        if state and self.game_status != "hosted":
            self.game_status = "ready"
            print("self.game_status:",self.game_status)
        elif not state and self.game_status != "hosted":
            self.game_status = "connected"
            print("self.game_status:", self.game_status, "Now")
    def vis_start_menu(self):
        self.strt.setVisible(True)
        self.strt.multiplayer_game_btn.setVisible(self.multiplaer)
        self.strt.single_game_btn.setVisible(not self.multiplaer)
        self.strt.multplayer_state = self.multiplaer
        self.lobby_setter_group.setVisible(False)
        self.user_label.setVisible(False)
        self._loby_line_edit.setVisible(False)
        self.plrs_in_lobby.setVisible(False)
        self._user_line_edit.setVisible(False)
        self._host_line_edit.setVisible(False)
        self._port_line_edit.setVisible(False)
        self.port_label.setVisible(False)
        self.host_label.setVisible(False)
        self.multiplayer_check_box.setVisible(False)
        self.username = self._user_line_edit.text()
        self.setWindowTitle(f'Dream Stars {self.username}')
        self._enter_name.setVisible(False)
        self.game_lobby_size = self._loby_line_edit.text()
        self.start_server()
        self.update()
    def start_server(self):

        if self._host_line_edit.text() == "127.0.0.1" or self._host_line_edit.text() == "localhost":
            print(self.start_server.__dict__)
            # start_sting = 'main_window.py {}'.format(self._user_line_edit.text())
            start_sting = '/Users/artur.abaidulov/Projects/DreamStars/Core/server.py'
            if self.server is None:  # No process running.
                #self.__setattr__(f"server{self.process_counter}", QProcess())
                self.server = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
                self.server.finished.connect(self.client_process_finished)  # Clean up once complete.
                self.server.start("python3.11", [start_sting])

    def client_process_finished(self):
        print("Client process finished.")
        self.server = None

    def multiplaer_set(self,state):
        self.multiplaer = state

    def create_connection(self):
        self._server_port = int(self._port_line_edit.text())
        self._server_host = self._host_line_edit.text()
        self.loby_size = int(self._loby_line_edit.text())
        self._timer = QTimer(self, interval=1000)
        self._timer.start()


        self._tcp_socket = QTcpSocket(self)
        self._block_size = 0
        self._message = "No message"

        self.message_to_send = self.msg_builder()
        self._timer.timeout.connect(self.request_new_fortune)
        self._tcp_socket.readyRead.connect(self.read_fortune)
        self._tcp_socket.errorOccurred.connect(self.display_error)





############ Functions ##########

    def map_gen(self):
        self.map.scene.clear()

        self.map.gen_star_data()
        self.map.drow_stars2()
        self.map.model = MyView(self.map.scene)
        self.map.model.setStyleSheet("background:black;")
        pass
    def map_move(self):
         self.map.time_print()
    def map_info(self):

            for i in self.map.model.scene().items():
                try:
                    print([i.id,i.data(0),round(i.boundingRect().x()),round(i.boundingRect().y())])
                except AttributeError:
                    #print("no id found")
                    print([i.data(0), round(i.boundingRect().x()), round(i.boundingRect().y())])

    def handleItemDoubleClicked(self, item):
            print(round(item.boundingRect().x()))
            print(round(item.boundingRect().y()))
            print(item.id)
            print(type(item))

    def item_selected(self, item):
        self.start_path = item
        print(item)
        print(type(item))

    def drow_path(self, item):
        if self.start_path is not None:
            print(self.start_path)
            print(item)
            print(type(item))
            self.map.drow_path(self.start_path["x"],item["x"],self.start_path["y"],item["y"])



##################  Network sender and reader Start #############
    def send_msg(self):
        """
        Формируем пакет для отправки сообщения
        Текст берется из self.message_to_send
        И отправляем пакет через созданный сокет
        """
        block = QByteArray()
        out = QDataStream(block, QIODevice.WriteOnly)
        out.setVersion(QDataStream.Qt_4_0)
        out.writeUInt16(0)
        out.writeString(self.message_to_send)
        out.device().seek(0)
        out.writeUInt16(block.size() - 2)
        self._tcp_socket.write(block)

    def request_new_fortune(self):
        """
        Открываем новый сокет для отправки сообщения на сервер
        И передаем инициативу уже отправщику сообщений

        """
        self._block_size = 0
        self._tcp_socket.abort()
        self._tcp_socket.connectToHost(self._server_host, int(self._server_port))
        self.send_msg()


    def read_fortune(self):
        """
        Получаем ответ от сервера отправляем его на обработку если же пакет закончился то возвращаемся

        """
        instr = QDataStream(self._tcp_socket)
        instr.setVersion(QDataStream.Qt_4_0)

        self._block_size = instr.readUInt16()
        self._message = instr.readString()
        print(self._message," -- from server")
        self.msg_parser(self._message)
        self.lobby_status()

        if self._block_size == 0:
            if self._tcp_socket.bytesAvailable() < 2:
                return

            self._block_size = instr.readUInt16()


        if self._tcp_socket.bytesAvailable() < self._block_size:
            return

        #self.send_msg()
    ##################  Network sender and reader End #############

    ##################  Msg parser and builder Start ##############


    def msg_builder(self):
        """

        """
        print(self.game_status)
        msg = {1: {"player_name": self.username, "game_status": self.game_status, "player_id": self.player_id},
               2: {"game_lobby_size": self.game_lobby_size, "map_size": self.map_size},
               3: {"server_turn": self.server_turn, "client_turn": self.client_turn, "chat_player_name": self.chat_player_name, "chat_message": self.chat_message},
               4: {"server_map_": self.server_map_, "client_map_": self.client_map_}
              }

        return str(msg)

    def msg_parser(self,msg):
        """
        """
        if msg is not None:
        #self.first_line(eval(msg)[1])
            self.second_line(eval(msg)[2])
            self.third_line(eval(msg)[3])
            self.fourth_line(eval(msg)[4])
            pass

    def second_line(self, data):
        self.game_lobby_size = data["game_lobby_size"]
        print("_+_+_+_+_",data["player_list"])
        self.map_size = data["map_size"]
        self.player_list = data["player_list"]
        pass

    def third_line(self, data):
        self.server_turn = data["server_turn"]
        if self.server_turn != 0:
            if self.server_turn == self.client_turn:
                self.game_status = "waiting"
            elif self.server_turn > self.client_turn:
                self.game_status = "playing"

        self.chat_player_name = data["chat_player_name"]
        self.chat_message = data["chat_message"]
        pass

    def fourth_line(self, data):
        self.client_map_ = data["client_map_"]
        self.server_map_ = data["server_map_"]
        pass
##################  Msg parser and builder End ##############



    def display_error(self, socketError):
        print(self.error_counter,"errors")

        if self.error_counter < 1:


            #self._tcp_socket.close()
            if socketError == QAbstractSocket.RemoteHostClosedError:

                pass
            elif socketError == QAbstractSocket.HostNotFoundError:
                self.error_counter += 1
                QMessageBox.information(self, "Fortune Client",
                                        "The host was not found. Please check the host name and "
                                        "port settings.")
            elif socketError == QAbstractSocket.ConnectionRefusedError:
                self.error_counter += 1
                QMessageBox.information(self, "Fortune Client",
                                        "The connection was refused by the peer. Make sure the "
                                        "fortune server is running, and check that the host name "
                                        "and port settings are correct.")
            else:
                reason = self._tcp_socket.errorString()
                self.error_counter += 1
                QMessageBox.information(self, "Fortune Client",
                                        f"The following error occurred: {reason}.")
        elif self.error_counter > 1:
            self.error_counter = 0
            self._timer.stop()



def main():

   app = QApplication(sys.argv)
   #username = str(sys.argv[1])
   try:
        ex = Main_Window(username=str(sys.argv[1]))
   except:
        ex = Main_Window()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()