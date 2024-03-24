import asyncio

counters = {
    'Counter 1': 0,
    'Counter 2': 0
}


max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}


async def counter(name: str, delay: int):
    while counters[name] != max_counts[name]:
        counters[name] += 1
        await asyncio.sleep(delay)
        print(f'{name}: {counters[name]}')


async def main():
    await asyncio.gather(*(asyncio.create_task(counter(f'Counter {i}', 1)) for i in range(1, 3)))


asyncio.run(main())
