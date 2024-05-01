import asyncio
import aiofiles
import aiocsv
import json
from aiofiles import os as aios
from time import monotonic

locker = asyncio.Semaphore(5)
start_time = monotonic()

results = {
    "Б/У": 0,
    "Новый": 0
}


async def worker(path_to_file: str):
    async with locker:
        async with aiofiles.open(path_to_file, encoding='windows-1251', newline='') as file:
            async for row in aiocsv.AsyncDictReader(file, delimiter=';', quotechar='"'):
                key = row.get('Состояние авто')
                value = row.get('Стоимость авто')
                if value is not None:
                    results[key] += int(value)


async def scan_directory(root_dir):
    for obj in await aios.scandir(root_dir):
        if obj.is_dir():
            await scan_directory(obj.path)
        elif obj.is_file():
            await worker(obj)


async def main():
    await scan_directory("Задача 3")


if __name__ == '__main__':
    asyncio.run(main())
    with open('result.json', 'w', encoding='utf-8') as result:
        json.dump(results, result, ensure_ascii=False, indent=4)
    print('Executing time:', monotonic() - start_time)
