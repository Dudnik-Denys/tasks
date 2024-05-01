import aiofiles
import asyncio
from aiofiles import os as aios
from time import monotonic

start = monotonic()
nums = {'odd': 0, 'even': 0}


async def worker(file):
    async with aiofiles.open('files/files/' + file, encoding='UTF-8') as f:
        data = await f.readline()
        data = int(data.strip())
        nums['odd' if data % 2 else 'even'] += data


async def main():
    files = await aios.listdir('files/files')
    await asyncio.gather(*[asyncio.create_task(worker(file)) for file in files])


if __name__ == '__main__':
    asyncio.run(main())
    print(nums)
    print('Executing time:', monotonic() - start)
