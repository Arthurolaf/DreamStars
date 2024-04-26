from PySide6 import QtCore, QtNetwork

class ClientManager(QtCore.QObject):
    def __init__(self, parent=None):
        super(ClientManager, self).__init__(parent)
        self._socket = QtNetwork.QTcpSocket(self)
        self._socket.stateChanged.connect(self.on_stateChanged)
        self._socket.readyRead.connect(self.on_readyRead)
        self._timer = QtCore.QTimer(self, interval=1000)
        self._timer_kill = QtCore.QTimer(self, interval=3000)
        self.msg = None
        self.response = None

    def launch(self, address=QtNetwork.QHostAddress.Any, port=9999):
        return self._socket.connectToHost(QtNetwork.QHostAddress(address), port)

    @QtCore.Slot(QtNetwork.QAbstractSocket.SocketState)
    def on_stateChanged(self, state):
        if state == QtNetwork.QAbstractSocket.ConnectedState:
                self._timer.start()
            print("connected")
        elif state == QtNetwork.QAbstractSocket.UnconnectedState:
            print("disconnected")
            #QtCore.QCoreApplication.quit()

    @QtCore.Slot()
    def sendMessage(self):
        #if self._socket.state() == QtNetwork.QAbstractSocket.ConnectedState:
            if self.msg is not None:
                self._socket.write(bytes(self.msg,"utf8"))



    @QtCore.Slot()
    def on_readyRead(self):
        if self.response is not None:
            self.msg = "stop"


    def return_response(self,msg):
        self.msg = msg
        self._timer.timeout.connect(self.sendMessage)

#        self._timer_kill.timeout.connect(self._socket.close())


if __name__ == '__main__':
    import sys
    import signal
    #signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtCore.QCoreApplication(sys.argv)
    address = '127.0.0.1'
    port = 9000
    server = ClientManager()
    server.launch(address, port)
    sys.exit(app.exec_())