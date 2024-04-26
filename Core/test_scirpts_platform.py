
import json
msg = {1: {"player_name": "John", "game_status": "connecting", "player_id": "91958ZDk"},
       2: {"game_lobby_size": "5", "map_size": "tiny", "player_list": {"p1:0,p2:1,p3:1"}},
       3: {"server_turn":1,"client_turn":1, "chat_player_name":"p2","chat_message":"blablabla"},
       4: {"server_map_":{"map_data_frame_from_server"},"client_map_":{"map_data_frame_from_server"}}
       }

# описание 1 ого поля
# {Имя игрока "player_name": "John" -- отображаемое имя игрока
# состояние игры
# "game_status":
# те кто полключился к лобби -- "connected" (in player_list = 1)
# те кто начал игру -- "hosted" (in player_list = 0)
# te кто подтвердил статус готовности -- "ready" (in player_list = 2)
# те кто отменил статус готовности -- "connected" (in player_list = 1)
# те кто играет в игру -- "playing" (in player_list = 3)
# те кто ожидает следующего хода -- (waiting)

#
class main_client():
    def __init__(self):
        self.game_name = "Walk in forest"
        self.username = "John"
        self.game_status = "hosted"
        self.player_id = "91958ZDk"
        self.game_lobby_size = "3"
        self.map_size = "tiny"
        self.player_list = {}
        self.client_turn = 0
        self.server_turn = 0
        self.chat_player_name = ""
        self.chat_message = ""
        self.client_map_ = {}
        self.server_map_ = {}
    def msg_builder(self):
        """
        """
        msg = {1: {"player_name": self.username, "game_status": self.game_status, "player_id": self.player_id},
               2: {"game_name": self.game_name,"game_lobby_size": self.game_lobby_size, "map_size": self.map_size, "player_list": self.player_list},
               3: {"server_turn": self.server_turn, "client_turn": self.client_turn, "chat_player_name": self.chat_player_name, "chat_message": self.chat_message},
               4: {"server_map_": self.server_map_, "client_map_": self.client_map_}
              }

        return str(msg)

    def msg_parser(self,msg):
        """
        """

        #self.first_line(eval(msg)[1])
        self.second_line(eval(msg)[2])
        self.third_line(eval(msg)[3])
        self.fourth_line(eval(msg)[4])
        pass

    def second_line(self, data):
        if self.game_status != "hosted":
            self.game_name = data["game_name"]
        self.game_lobby_size = data["game_lobby_size"]
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


class main_server():

    def __init__(self):
        self.username = "John"
        self.game_status = "connected"
        self.player_id = "91958ZDk"
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
        #print(eval(msg))

        self.first_line(eval(msg)[1])
        self.second_line(eval(msg)[2],eval(msg)[1])
        self.third_line(eval(msg)[3],eval(msg)[1])
        self.fourth_line(eval(msg)[4],eval(msg)[1])
        pass

    def first_line(self,data):
        self.player_list[data["player_name"]] = data["game_status"]
        #print(self.player_list)
    def second_line(self, data,pdata):
        if pdata["game_status"] == "hosted":
            self.game_lobby_size = data["game_lobby_size"]
            self.map_size = data["map_size"]
        pass

    def third_line(self, data,pdata):
        self.server_turn = 0
        self.turn_check[pdata["player_name"]] =  data["client_turn"]
        self.chat_player_name = data["chat_player_name"]
        self.chat_message = data["chat_message"]
        pass
    def fourth_line(self, data,pdata):
        self.client_map_ = {pdata["player_name"]:data["client_map_"]}
        self.server_map_ = {pdata["player_name"]:"map_data"}
        pass

client = main_client()
client2 = main_client()
client2.username = "Olaf"
client2.game_status = "connected"
client2.player_id = "21948Z98"
client2.game_lobby_size = ""
client2.map_size = ""

client3 = main_client()
client3.username = "Eddy"
client3.game_status = "connected"
client3.player_id = "2587D286"
client3.game_lobby_size = ""
client3.map_size = ""

server = main_server()

client_msg = client.msg_builder()
server.msg_parser(client_msg)
response = eval(server.msg_builder())

client2_msg = client2.msg_builder()
server.msg_parser(client2_msg)
response2 = eval(server.msg_builder())

client3_msg = client3.msg_builder()
server.msg_parser(client3_msg)
response3 = eval(server.msg_builder())


client.msg_parser(str(response))
print(client.msg_builder())
client2.msg_parser(str(response2))
print(client2.msg_builder())
client3.msg_parser(str(response3))
print(client3.msg_builder())
