import json
import os
import asyncio
import aiofiles
import aiocsv
from datetime import datetime


def prepare_valid_data(path: str) -> list:
    data = []
    files = os.scandir(path)
    for file in files:
        with open(file.path, 'r', encoding='utf-8') as f:
            data.extend(json.load(f))
    data = [el for el in data if el["HTTP-статус"] == 200]
    for el in data:
        d, t = el["Время и дата"].split()
        years, months, days = d.split('-')
        el["Время и дата"] = datetime.strptime(f'{days}.{months}.{years} {t}', '%d.%m.%Y %H:%M:%S')
    data = sorted(data, key=lambda el: el["Время и дата"])
    for el in data:
        el["Время и дата"] = el["Время и дата"].strftime('%d.%m.%Y %H:%M:%S')
    return data


async def main(data: list) -> None:
    async with aiofiles.open('result.csv', 'w', encoding='utf-8-sig', newline='') as result:
        fields = ["Время и дата", "IP-адрес", "User-Agent", "Запрошенный URL", "HTTP-статус", "Реферер", "Cookie",
                  "Размер страницы и заголовки ответа", "Метод запроса", "Информация об ошибке"]
        writer = aiocsv.AsyncDictWriter(result, fieldnames=fields, delimiter=';', quotechar='"', lineterminator='\n')
        await writer.writeheader()
        await writer.writerows(data)


if __name__ == '__main__':
    temp_data = prepare_valid_data('logs')
    asyncio.run(main(temp_data))
    print(temp_data)
