import asyncio
import aiocsv
import aiofiles
import os
import glob
from aiofiles import os as aios
from time import monotonic

start = monotonic()
result = {'total_sum': 0}


async def scan_folder(folder: str):
    files = await aios.listdir(folder)
    await asyncio.gather(*[asyncio.create_task(worker(folder, file)) for file in files])


async def worker(folder_name, file_name):
    async with aiofiles.open(folder_name + '/' + file_name, encoding='UTF-8') as csv_file:
        async for row in aiocsv.AsyncReader(csv_file):
            result['total_sum'] += int(row[0])


async def main():
    folders = glob.glob(os.path.join('5000folder', '*'))
    async with asyncio.TaskGroup() as group:
        [group.create_task(scan_folder(folder)) for folder in folders]


if __name__ == '__main__':
    asyncio.run(main())
    print(result)
    print('Executing time:', monotonic() - start)
