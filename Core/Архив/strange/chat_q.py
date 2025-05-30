import asyncio

class client():
    def __init__(self, command=None):
        async def telnet_client(host: str, port: int, username: str, password: str) -> None:
            reader, writer = await asyncio.open_connection(host, port)
            print(f"connected to ({host}, {port})")

            # Login to the server, if the server requires authentication
            """ await writer.write(f"{username}\n".encode())
                await writer.write(f"{password}\n".encode()) """

            while True:
                self.command = input("\nEnter a command: ")
                if command != "exit":
                    if not command:
                        print("[No command] ...closing connection ")
                        break
                    writer.write(f"{command}\n".encode())
                    data = await reader.read(100000)
                    print(data.decode().strip())
                else:
                    break

        # there is a telnet server (telnet_server.py) listening on localhost port=23
        asyncio.run(telnet_client("127.0.0.1", 2000, "username", "password"))

client