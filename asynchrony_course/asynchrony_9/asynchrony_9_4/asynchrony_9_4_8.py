import asyncio

users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']


async def connect(user: str, lock: asyncio.Condition) -> None:
    async with lock:
        print(f'Пользователь {user} ожидает доступа к базе данных')
    await asyncio.sleep(1)
    print(f'Пользователь {user} подключился к БД\nПользователь {user} отключается от БД')


async def main() -> None:
    condition = asyncio.Condition()
    await asyncio.gather(*[asyncio.create_task(connect(usr, condition)) for usr in users])


asyncio.run(main())
