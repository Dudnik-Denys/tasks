import asyncio
import aiofiles
import aiocsv
import os
import glob
import json
from aiofiles import os as aios
from time import monotonic

start = monotonic()
cities = glob.glob(os.path.join('region_student', '*/*'))
results = []


async def scan_city(path_to_city: str, locker: asyncio.Semaphore):
    schools = await aios.listdir(path_to_city)
    await asyncio.gather(*[asyncio.create_task(worker(path_to_city + '/' + school, locker)) for school in schools])


async def worker(path, semaphore: asyncio.Semaphore):
    async with semaphore:
        async with aiofiles.open(path, encoding='utf-8-sig') as csv_file:
            async for row in aiocsv.AsyncDictReader(csv_file):
                if row['Балл ЕГЭ'] == '100':
                    results.append(row)


async def main():
    semaphore = asyncio.Semaphore(10)
    async with asyncio.TaskGroup() as task_group:
        [task_group.create_task(scan_city(city, semaphore)) for city in cities]


if __name__ == '__main__':
    asyncio.run(main())
    results = sorted(results, key=lambda x: x['Телефон для связи'])

    with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    print('Executing time:', monotonic() - start)
