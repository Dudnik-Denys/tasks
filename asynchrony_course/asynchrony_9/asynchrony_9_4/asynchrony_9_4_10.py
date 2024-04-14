import asyncio

stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

condition = asyncio.Condition()
stone_event = asyncio.Event()
metal_event = asyncio.Event()
cloth_event = asyncio.Event()

resources = {
    'камень': 0,
    'металл': 0,
    'ткань': 0
}


async def gather_stone():
    # Добываем камень, 10ед каждую сек.
    while True:
        await asyncio.sleep(1)
        if stone_event.is_set():
            break
        async with condition:
            resources['камень'] += 10
            print(f'Добыто 10 ед. камня. На складе {resources["камень"]} ед.')
            condition.notify()


async def gather_metal():
    # Добываем металл, 6ед каждую сек.
    while True:
        await asyncio.sleep(1)
        if metal_event.is_set():
            break
        async with condition:
            resources['металл'] += 6
            print(f'Добыто 6 ед. металла. На складе {resources["металл"]} ед.')
            condition.notify()


async def gather_cloth():
    # Добываем ткань, 8ед каждую сек.
    while True:
        await asyncio.sleep(1)
        if cloth_event.is_set():
            break
        async with condition:
            resources['ткань'] += 8
            print(f'Добыто 8 ед. ткани. На складе {resources["ткань"]} ед.')
            condition.notify()


async def craft_stone_items():
    # Мастерская по крафту из камня
    for key, value in stone_resources_dict.items():
        async with condition:
            await condition.wait_for(lambda: value <= resources['камень'])
            resources['камень'] -= value
            print(f'Изготовлен {key} из камня.')
    stone_event.set()


async def craft_metal_items():
    # Мастерская по крафту из мателла
    for key, value in metal_resources_dict.items():
        async with condition:
            await condition.wait_for(lambda: value <= resources['металл'])
            resources['металл'] -= value
            print(f'Изготовлен {key} из металла.')
    metal_event.set()


async def craft_cloth_items():
    # Мастерская по крафту из ткани
    for key, value in cloth_resources_dict.items():
        async with condition:
            await condition.wait_for(lambda: value <= resources['ткань'])
            resources['ткань'] -= value
            print(f'Изготовлен {key} из ткани.')
    cloth_event.set()


async def main():
    await asyncio.gather(gather_stone(), gather_metal(), gather_cloth(), craft_stone_items(), craft_metal_items(),
                         craft_cloth_items())


asyncio.run(main())
