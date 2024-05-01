import asyncio
import aiocsv
import aiofiles
import json


async def main():
    async with aiofiles.open('adress_1000000.csv', encoding='utf-8-sig') as csv_file:
        csv_reader = aiocsv.AsyncDictReader(csv_file, delimiter=';')
        result = [row async for row in csv_reader]
        return result


if __name__ == '__main__':
    res = asyncio.run(main())
    with open('result.json', 'w', encoding='utf-8') as json_file:
        json.dump(res, json_file, ensure_ascii=False, indent=4)
