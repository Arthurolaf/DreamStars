import asyncio

async def inside_client(host: str, port: int, username: str, password: str) -> None:
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
async def start_client():
    try:
        client = inside_client("127.0.0.1", 2000, "username", "password")
        print("CLient started")
        await client
    except:
        pass
asyncio.run(start_client())


def run_command(com: str) -> None:
    try:
        if com == "Hi":
            return f"Hello"
        else:
            return "Oh No"
    except Exception as ex:
        print("exception occurred")
        return f"   [subprocess broke]"


async def handle_client(reader, writer):
    print(f"Connected to {writer.get_extra_info('peername')}")

    while True:
        data = await reader.read(100000)
        message = data.decode().strip()
        if not message:
            break
        print(f"Received message: {message}")
        res = run_command(message)
        writer.write(res.encode())

    print(f"Closing connection {writer.get_extra_info('peername')}")
    writer.close()


async def start_server():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 2001)
    print("Server started")
    await server.serve_forever()

asyncio.run(start_server())