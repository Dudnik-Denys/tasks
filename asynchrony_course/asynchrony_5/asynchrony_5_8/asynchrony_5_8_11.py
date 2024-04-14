import asyncio


async def activate_portal(x: int) -> int:
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x: int) -> int:
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def recharge_teleportation(x: int) -> int:
    print(f'Подзарядка портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 3


async def check_portal_stability(x: int) -> int:
    print(f'Проверка стабильности портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 4


async def restore_portal(x: int) -> int:
    print(f'Восстановление портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 5


async def close_portal(x: int) -> int:
    print(f'Закрытие портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    activate = await activate_portal(2)
    tasks = [asyncio.create_task(perform_teleportation(3), name='телепортации'),
             asyncio.create_task(recharge_teleportation(4), name='подзарядки'),
             asyncio.create_task(check_portal_stability(5), name='проверки стабильности'),
             asyncio.create_task(restore_portal(6), name='восстановления')]
    await asyncio.gather(*tasks)
    close = await close_portal(7)
    print(f'Результат активации портала: {activate} единиц энергии')

    for task in tasks:
        portal = ' портала' if task.get_name() in ['подзарядки', 'восстановления'] else ''
        energy = 'времени' if task.get_name() in ['телепортации', 'проверки стабильности'] else 'энергии'
        print(f'Результат {task.get_name()}{portal}: {task.result()} единиц {energy}')

    print(f'Результат закрытия портала: {close} единиц времени')


asyncio.run(portal_operator())
