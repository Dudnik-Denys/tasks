import asyncio
import random

server_names = {
        "1": "Server_Alpha", "2": "Server_Beta", "3": "Server_Gamma",
        "4": "Server_Delta", "5": "Server_Epsilon"}


async def load_data(server):
    print(f'Загрузка данных с сервера {server} началась')
    await asyncio.sleep(random.randint(1, 5))
    print(f'Загрузка данных с сервера {server} завершена')


async def main(n):
    async with asyncio.TaskGroup() as group:
        [group.create_task(load_data(data)) for data in server_names.values()]


asyncio.run(main(5))
