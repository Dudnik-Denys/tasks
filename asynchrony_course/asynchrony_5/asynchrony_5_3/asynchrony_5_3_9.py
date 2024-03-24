import asyncio


async def coroutine_1():
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(1.5)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 1")


async def coroutine_2():
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(1)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 2")


async def coroutine_3():
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(.5)  # Подберите необходимую задержку
    print("Второе сообщение от корутины 3")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )


asyncio.run(main())
