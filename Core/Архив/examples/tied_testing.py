import uuid
from PySide6 import QtCore, QtNetwork

class ServerManager(QtCore.QObject):
    def __init__(self, parent=None):
        super(ServerManager, self).__init__(parent)
        self._server = QtNetwork.QTcpServer(self)
        self._server.newConnection.connect(self.on_newConnection)
        self._clients = {}

    def launch(self, address=QtNetwork.QHostAddress.Any, port=9999):
        print("starting server")
        return self._server.listen(QtNetwork.QHostAddress(address), port)

    @QtCore.Slot()
    def on_newConnection(self):
        socket = self._server.nextPendingConnection()

        socket.readyRead.connect(self.on_readyRead)
        if socket not in self._clients:
            self._clients[socket] = uuid.uuid4()

    @QtCore.Slot()
    def on_readyRead(self):
        socket = self.sender()
        resp = socket.readAll()
        print(type(resp))
#        answer = str(resp)
#        print(type(answer))
        answer = bytes(resp).decode(encoding="utf8")
        code = self._clients[socket]
        #resp = bytes.decode(resp,"utf8")
        print("From[{}]- message: {}".format(code, resp))
        socket.write(bytes(f"Server: {answer}","utf8"))

if __name__ == '__main__':
    import sys
    import signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtCore.QCoreApplication(sys.argv)

    address = '127.0.0.1'
    port = 9000
    server = ServerManager()
    if not server.launch(address, port):
        sys.exit(-1)
    sys.exit(app.exec())