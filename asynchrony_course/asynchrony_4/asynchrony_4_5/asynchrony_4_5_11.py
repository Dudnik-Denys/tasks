import asyncio

global_counter = 0


async def increment(lock: asyncio.Lock):
    async with lock:
        global global_counter
        temp = global_counter
        await asyncio.sleep(.01)
        global_counter = temp + 2.39


async def main():
    lock = asyncio.Lock()
    await asyncio.gather(*[increment(lock) for x in range(99)])


asyncio.run(main())
print(f"global_counter: {round(global_counter,2)}")
