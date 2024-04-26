from PySide6.QtNetwork import QAbstractSocket, QTcpSocket
from PySide6.QtCore import QObject,QDataStream,QTimer,QByteArray,QIODevice
from PySide6.QtWidgets import QPushButton,QApplication,QMessageBox,QDialog,QWidget,QVBoxLayout
class Client(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._server_port = 2000
        self._server_host = "127.0.0.1"
        self._client_port = 2001
        self._block_size = 0
        self._message = 'Test client'

        self._status_label ="This examples requires that you run the Fortune Server example as well."

        self._tcp_socket = QTcpSocket(self)
        self._layout = QVBoxLayout(self)
        self._get_fortune_button = QPushButton("Get Fortune")
        self._layout.addWidget(self._get_fortune_button)
        self._get_fortune_button.clicked.connect(self.request_new_fortune)

        self._tcp_socket.readyRead.connect(self.read_fortune)
        self._tcp_socket.errorOccurred.connect(self.display_error)

    def send_msg(self):
        block = QByteArray()
        out = QDataStream(block, QIODevice.WriteOnly)
        out.setVersion(QDataStream.Qt_4_0)
        out.writeUInt16(0)
        #msg = self._message
        print("msg:",self._message)
        out.writeString(self._message)
        out.device().seek(0)
        out.writeUInt16(block.size() - 2)
       # out.device().seek(0)
       # print("rUint16: ",out.readUInt16())
        #print(out.readString())
        #out.writeUInt16(block.size() - 2)

        self._tcp_socket.write(block)


    def request_new_fortune(self):

        print(self._block_size, "test")
        self._block_size = 0
        self._tcp_socket.abort()
        self._tcp_socket.connectToHost(self._server_host,self._server_port)
        self.send_msg()
    def read_fortune(self):
        instr = QDataStream(self._tcp_socket)
        instr.setVersion(QDataStream.Qt_4_0)

        self._block_size = instr.readUInt16()
        self._message = instr.readString()
        print(self._message)
        print(self._block_size)
        if self._block_size == 0:
            if self._tcp_socket.bytesAvailable() < 2:
                return

            self._block_size = instr.readUInt16()
            print(self._block_size)
            #self._message = instr.readString()

            #self._message = message
            #print(self._message)

        if self._tcp_socket.bytesAvailable() < self._block_size:
            return




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

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    client = Client()

    client.show()

    sys.exit(app.exec())

