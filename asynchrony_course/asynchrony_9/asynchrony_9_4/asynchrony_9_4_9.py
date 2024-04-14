import asyncio

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}

resources = {'wood': 0}


async def gather_wood(condition: asyncio.Condition, terminate_event: asyncio.Event) -> None:
    while True:
        await asyncio.sleep(1)
        print('Блокировка добычи', condition.locked())
        if terminate_event.is_set():
            break
        async with condition:
            resources['wood'] += 2
            print(f"Добыто 2 ед. дерева. На складе {resources['wood']} ед.")
            condition.notify()
            await asyncio.sleep(0.2)
            print('Блокировка добычи', condition.locked())


async def craft_item(condition: asyncio.Condition, terminate_event: asyncio.Event) -> None:
    for key, value in wood_resources_dict.items():
        print('Блокировка крафта', condition.locked())
        async with condition:
            print('Блокировка крафта', condition.locked())
            await condition.wait_for(lambda: value <= resources['wood'])
            print('Блокировка крафта', condition.locked())
            resources['wood'] -= value
            print(f"Изготовлен {key}.")
    print('Блокировка крафта', condition.locked())
    terminate_event.set()


async def main() -> None:
    condition = asyncio.Condition()
    event = asyncio.Event()
    await asyncio.gather(craft_item(condition, event), gather_wood(condition, event))


if __name__ == '__main__':
    asyncio.run(main())
