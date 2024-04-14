import asyncio
from itertools import count

robot_names = {0: 'Электра', 1: 'Механикс', 2: 'Оптимус', 3: 'Симулакр', 4: 'Футуриус'}
visits = count(1)


async def executor(lock: asyncio.Lock, robot_id: int, robot_name: str) -> None:
    global visits
    print(f'Робот {robot_name}({robot_id}) передвигается к месту A')

    async with lock:
        await asyncio.sleep(1)
        print(f'Робот {robot_name}({robot_id}) достиг места A. Место A посещено {next(visits)} раз')


async def main():
    locker = asyncio.Lock()
    await asyncio.gather(*[asyncio.create_task(executor(locker, key, value)) for key, value in robot_names.items()])


asyncio.run(main())
