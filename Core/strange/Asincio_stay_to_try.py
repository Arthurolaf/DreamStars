import asyncio


# имитация  асинхронного соединения с некой периферией
async def get_conn(host, port):
    class Conn:
        async def put_data(self):

                data = input("Введите сообщение")
                print('Отправка данных...')

                import socket
                try:
                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.s.connect((host, 8080))
                except:
                    print("we have problev with connection to server")
                try:
                    self.s.send(bytes(data, "utf8"))  # send message to the server in encode form.
                except:
                    print("server not started pass")
                print('Данные отправлены.')

        async def get_data(self):
            print('Получение данных...')
            #while True:
            try:
                msg = self.s.recv(1024).decode()  # receive messages and decode it into string.
                if msg is not None or msg != '':
                    print(msg, "delivered")
            except Exception:
                print("There is an Error Receiving Message")
            #await asyncio.sleep(2)
        print('Данные получены.')

        async def close(self):
            print('Завершение соединения...')
            await asyncio.sleep(2)
            print('Соединение завершено.')

    print('Устанавливаем соединение...')
    await asyncio.sleep(2)
    print('Соединение установлено.')
    return Conn()


class Connection:
    # этот конструктор будет выполнен в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', 9001) as conn:

        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        # операции отправки и получения данных выполняем конкурентно
            await send_task
            await receive_task



asyncio.run(main())