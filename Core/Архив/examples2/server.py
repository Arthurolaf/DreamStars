import asyncio

#
# class EchoServerProtocol(asyncio.Protocol):
#     def connection_made(self, transport):
#         peername = transport.get_extra_info('peername')
#         print('Connection from {}'.format(peername))
#         self.transport = transport
#
#     def data_received(self, data):
#         message = data.decode()
#         print('Data received: {!r}'.format(message))
#
#         print('Send: {!r}'.format(message))
#         self.transport.write(data)
#
#         print('Close the client socket')
#         self.transport.close()
#
#
#
# async def main():
#     # Get a reference to the event loop as we plan to use
#     # low-level APIs.
#     loop = asyncio.get_running_loop()
#
#     server = await loop.create_server(
#         lambda: EchoServerProtocol(),
#         '127.0.0.1', 8888)
#
#     async with server:
#         await server.serve_forever()
#
#
# asyncio.run(main())
#


from PyQt5 import QtCore


class UDPserver(QtCore.QObject):
    dataChanged = QtCore.pyqtSignal(float, float, float, float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._transport = None
        self._counter_message = 0

    @property
    def transport(self):
        return self._transport

    def connection_made(self, transport):
        self._transport = transport
        self.peername = transport.get_extra_info('peername')
    def datagram_received(self, data, addr):
        self._counter_message += 1
        print("#Num of Mssg Received: {}".format(self._counter_message))
        message = data.decode()
        new_text_str = message.split( "/")
        try:
            new_text = float(new_text_str)
            peename = str(self.peername)
            self.dataChanged.emit(new_text,peename)
        except ValueError as e:
            print(e)