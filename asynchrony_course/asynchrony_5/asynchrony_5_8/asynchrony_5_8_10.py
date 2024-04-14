import asyncio


async def activate_portal(x: int | float) -> int | float:
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x: int | float) -> int | float:
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    activate = await asyncio.ensure_future(activate_portal(2))
    perform = await asyncio.ensure_future(perform_teleportation(activate if activate <= 4 else 1))
    print(f'Результат активации портала: {activate} единиц энергии\n'
          f'Результат телепортации: {perform} единиц времени')


asyncio.run(portal_operator())
