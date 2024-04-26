import asyncio
class client_server():
    def __init__(self):
        self.sever_started = False
        self.command = "None"
        #self.cleint_started = False
    async def inside_client(self, host: str, port: int, username: str, password: str) -> None:
        reader, writer = await asyncio.open_connection(host, port)
        print(f"connected to ({host}, {port})")

        # Login to the server, if the server requires authentication
        """ await writer.write(f"{username}\n".encode())
            await writer.write(f"{password}\n".encode()) """

        while True:
            command = input("\nEnter a command: ")
            if not command:
                print("[No command] ...closing connection ")
                break
            writer.write(f"{command}\n".encode())
            data = await reader.read(100000)
            print(data.decode().strip())

    # there is a telnet server (telnet_server.py) listening on localhost port=23
    async def start_client(self):
        if self.sever_started:
            try:
                client = self.inside_client("127.0.0.1", 2001, "username", "password")
                print("CLient started")
                await client
            except:
                pass

cleint_ = client_server()
async def change_send():
    cleint_.command = input("Введите число")

loop = asyncio.get_event_loop()
loop.create_task(change_send())
loop.run_until_complete(cleint_.start_client())
loop.run_forever()

#asyncio.run(cleint_.start_client())

    #
    # def run_command(self, com: str) -> None:
    #     try:
    #         if com == "Hi":
    #             return f"Hello"
    #         else:
    #             return "Oh No"
    #     except Exception as ex:
    #         print("exception occurred")
    #         return f"   [subprocess broke]"
    #
    #
    # async def handle_client(self, reader, writer):
    #     print(f"Connected to {writer.get_extra_info('peername')}")
    #
    #     while True:
    #         data = await reader.read(100000)
    #         message = data.decode().strip()
    #         if not message:
    #             break
    #         print(f"Received message: {message}")
    #         res = self.run_command(message)
    #         writer.write(res.encode())
    #
    #     print(f"Closing connection {writer.get_extra_info('peername')}")
    #     writer.close()
    #
    #
    # async def start_server(self):
    #     self.sever_started = True
    #     server = await asyncio.start_server(self.handle_client, "127.0.0.1", 2000)
    #     print("Server started")
    #     await server.serve_forever()
    #
    # asyncio.run(start_server())