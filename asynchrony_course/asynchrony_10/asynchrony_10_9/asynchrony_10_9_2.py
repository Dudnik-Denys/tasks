import asyncio
import aiofiles
import re
import json
from aiofiles import os as aios
from time import monotonic


start = monotonic()
results = {}


async def lines_generator(lines):
    for line in lines:
        yield line


async def worker(file):
    async with aiofiles.open('chat_log/' + file, encoding='UTF-8') as f:
        lines = await f.readlines()
        async for line in lines_generator(lines):
            _, name, msg = re.split(r': | -', line.strip())
            name, cost = name.lstrip(), len(msg) * 0.03
            results[name] = results.get(name, 0) + cost


async def main():
    files = await aios.listdir('chat_log')
    async with asyncio.TaskGroup() as group:
        [group.create_task(worker(file)) for file in files]
    for key, value in results.items():
        results[key] = str(round(value, 2)) + 'р'


if __name__ == '__main__':
    asyncio.run(main())
    print(json.dumps(results, indent=4, ensure_ascii=False))
    print('Executing time:', monotonic() - start)
