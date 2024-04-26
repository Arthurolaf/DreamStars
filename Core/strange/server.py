# importing required libraries.
import socket
from threading import Thread
import sys
import atexit
import signal

# define IP and port for server.
host = "localhost"
port = 8080

clients = {}  # clients dict to store information about clients connection.

# create socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set configuration so that many clients can request on one single port.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the IP and port to the socket object.
sock.bind((host, port))


# function to get name and broadcast to all others.
def handle_clients(conn):
    # get client's name from it's connection
    name = conn.recv(1024).decode()

    # send the client a welcome message
    welcome = f"Welcome {name}. Good to see you :)"
    conn.send(bytes(welcome, "utf8"))

    # create a message of recently added clients
    msg = name + " has recently joined us"

    # send the message to the all connected clients.
    broadcast(bytes(msg, "utf8"))

    # save the newly added clients info to the dictionary
    clients[name] = conn

    # receive message from client in loop and broadcast it.
    while True:
        msg = conn.recv(1024)
        print(msg)
        broadcast(msg, name + ":")


# send the message to the all connected clients.
def broadcast(msg, prefix=""):
    for client, connections in clients.items():  # clients is dict that save client's connection info
        try:
            connections.send(bytes(prefix, "utf8") + msg)
            clientslast = clients
        except BrokenPipeError:
            #print(clientslast)
            print(clients)

            print("Какой-то злодей отвалился ждемс")

def accept_client_connection():
    while True:  # accept client's request
        client_conn, client_address = sock.accept()  # accept client request
        print(client_address, " has Connected")

        # send a welcome message to the client and ask for name from it.
        client_conn.send(bytes("Welcome to the chat room, Please type your name to continue", "utf8"))

        # start the handle clients function in a thread.
        Thread(target=handle_clients, args=(client_conn,)).start()



if __name__ == "__main__":
    def exit_handler():
        print("Cleaning up")

        try:
            broadcast("Server is close", ":")

        except:

            print("can't send broadcast msg")



    def kill_handler(*args):
        broadcast(b"Server is close", ":")
        for client, connections in clients.items():
            connections.shutdown(1)
            connections.close()
        sys.exit(0)


    atexit.register(exit_handler)
    signal.signal(signal.SIGINT, kill_handler)
    signal.signal(signal.SIGTERM, kill_handler)
    #signal.signal(signal.SIGKILL, kill_handler)
    # server is listening........
    sock.listen(3)  # here we are accepting max of three clients at once.
    print("listening on port : ", port, "......")

    # start the accept function into thread for handle multiple request at once.
    t = Thread(target=accept_client_connection)

    t.start()  # start thread
    t.join()  # thread wait for main thread to exit.


