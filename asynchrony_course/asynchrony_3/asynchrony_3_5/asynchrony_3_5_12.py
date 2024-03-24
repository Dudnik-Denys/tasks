import asyncio


async def func(n):
    print(f'Coroutine {n} is done')


async def main():
    tasks = [asyncio.create_task(func(n)) for n in range(1, 4)]
    await asyncio.gather(*tasks)


asyncio.run(main())
