import asyncio


async def coroutine_1():
    await asyncio.sleep(1)  # Задержка для первого сообщения
    print("Сообщение 1 от корутины 1")
    await asyncio.sleep(2)  # Задержка для второго сообщения
    print("Сообщение 2 от корутины 1")


async def coroutine_2():
    await asyncio.sleep(1)
    print("Сообщение 1 от корутины 2")
    await asyncio.sleep(2)
    print("Сообщение 2 от корутины 2")


async def coroutine_3():
    await asyncio.sleep(1)
    print("Сообщение 1 от корутины 3")
    await asyncio.sleep(2)
    print("Сообщение 2 от корутины 3")


async def coroutine_4():
    await asyncio.sleep(1)
    print("Сообщение 1 от корутины 4")
    await asyncio.sleep(2)
    print("Сообщение 2 от корутины 4")


async def coroutine_5():
    await asyncio.sleep(1)
    print("Сообщение 1 от корутины 5")
    await asyncio.sleep(2)
    print("Сообщение 2 от корутины 5")


async def coroutine_6():
    await asyncio.sleep(1)
    print("Сообщение 1 от корутины 6")
    await asyncio.sleep(2)
    print("Сообщение 2 от корутины 6")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
        coroutine_4(),
        coroutine_5(),
        coroutine_6(),
    )


asyncio.run(main())
