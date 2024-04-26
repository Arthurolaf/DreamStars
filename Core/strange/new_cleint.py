# import required libraries
import socket
from threading import Thread
class ConnectorToServer():
    def __init__(self, host="127.0.0.1",port=8080):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((host, 8080))
        except:
            print("we have problev with connection to server")
        self.receive_thread = Thread(target=self.receive)
        self.receive_thread.start()
        # receive messages in loop and display in tkinter window
    def receive(self):
        while True:
            try:
                msg = self.s.recv(1024).decode()  # receive messages and decode it into string.
                #print(msg, "delivered")
            except Exception:
                print("There is an Error Receiving Message")

        # get message from tkinter entry field and send the message to the server
    def send(self,msg):
        try:
            self.s.send(bytes(msg, "utf8")) # send message to the server in encode form.
        except:
            print("server not started pass")
        #send_button = Button(window, text="Send", font="Aerial", fg="black", bg="blue", command=send)
        #send_button.pack()


def send_msg(msg):
    connection = ConnectorToServer()
    connection.send(msg)
    #connection = None

#send_msg("test")