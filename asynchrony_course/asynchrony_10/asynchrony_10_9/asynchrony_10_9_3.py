import asyncio
import aiocsv
import aiofiles
from aiofiles import os as aios
from time import monotonic

start = monotonic()
result = {'total_sum': 0}


async def worker(file_name):
    async with aiofiles.open('5000csv/' + file_name, encoding='UTF-8') as csv_file:
        async for row in aiocsv.AsyncReader(csv_file):
            result['total_sum'] += int(row[0])


async def main():
    files = await aios.listdir('5000csv')
    async with asyncio.TaskGroup() as group:
        [group.create_task(worker(file)) for file in files]


if __name__ == '__main__':
    asyncio.run(main())
    print(result)
    print('Executing time:', monotonic() - start)
