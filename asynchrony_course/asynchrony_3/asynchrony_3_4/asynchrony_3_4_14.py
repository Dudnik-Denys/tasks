import asyncio


async def generate(num: int):
    print(f'Корутина generate с аргументом {num}')


async def main():
    await asyncio.gather(*[asyncio.create_task(generate(i)) for i in range(10)])


asyncio.run(main())
