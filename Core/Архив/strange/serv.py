import asyncio
import subprocess


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
        res = input("Что ответим клиенту?")
        writer.write(res.encode())

    print(f"Closing connection {writer.get_extra_info('peername')}")
    writer.close()


async def start_server():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 2001)
    print("Server started")
    await server.serve_forever()

asyncio.run(start_server())