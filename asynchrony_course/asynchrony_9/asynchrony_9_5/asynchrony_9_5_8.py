import asyncio

users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
         "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]

semaphore = asyncio.Semaphore(3)
data = {'requests': 0}


async def make_request(name: str) -> None:
    async with semaphore:
        print(f'Пользователь {name} делает запрос')
        data['requests'] += 1
        await asyncio.sleep(1)
        print(f'Запрос от пользователя {name} завершен')
        print(f'Всего запросов: {data["requests"]}')


async def main() -> None:
    await asyncio.gather(*[asyncio.create_task(make_request(user)) for user in users])


asyncio.run(main())
