import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup
from time import monotonic

start = monotonic()
base_url = 'https://asyncio.ru/zadachi/2/html/'


async def get_soup(url: str, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> BeautifulSoup:
    async with semaphore:
        async with session.get(url) as response:
            return BeautifulSoup(await response.text(), 'lxml')


async def main() -> int:
    semaphore = asyncio.Semaphore(10)
    async with aiofiles.open('file.txt', encoding='utf-8') as file:
        file_data = [line.strip() for line in await file.readlines()]

    async with aiohttp.ClientSession() as session:
        soups = await asyncio.gather(*[asyncio.create_task(get_soup(base_url + url + '.html', session, semaphore)) for
                                       url in file_data])
        return sum([int(soup.select_one('#number').text) for soup in soups])


if __name__ == '__main__':
    print(asyncio.run(main()))
    print('Executing time:', monotonic() - start)
