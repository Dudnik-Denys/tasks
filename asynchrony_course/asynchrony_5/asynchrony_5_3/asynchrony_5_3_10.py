import asyncio


async def coroutine_1():
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(1)  # Первая задержка
    print("Второе сообщение от корутины 1")
    await asyncio.sleep(2)  # Вторая задержка
    print("Третье сообщение от корутины 1")
    await asyncio.sleep(3)  # Третья задержка
    print("Четвертое сообщение от корутины 1")


async def coroutine_2():
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(1)  # Первая задержка
    print("Второе сообщение от корутины 2")
    await asyncio.sleep(2)  # Вторая задержка
    print("Третье сообщение от корутины 2")
    await asyncio.sleep(3)  # Третья задержка
    print("Четвертое сообщение от корутины 2")


async def coroutine_3():
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(1)  # Первая задержка
    print("Второе сообщение от корутины 3")
    await asyncio.sleep(2)  # Вторая задержка
    print("Третье сообщение от корутины 3")
    await asyncio.sleep(3)  # Третья задержка
    print("Четвертое сообщение от корутины 3")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )


asyncio.run(main())
