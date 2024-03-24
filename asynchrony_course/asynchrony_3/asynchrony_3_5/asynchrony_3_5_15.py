import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}


async def counter(name: str, delay: int):
    while counters[name] != max_counts[name]:
        counters[name] += 1
        await asyncio.sleep(delay)
        print(f'{name}: {counters[name]}')


async def main():
    await asyncio.gather(*(asyncio.create_task(counter(f'Counter {i}', delays[f'Counter {i}'])) for i in range(1, 4)))


asyncio.run(main())
