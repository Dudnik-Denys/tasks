import asyncio
import aiohttp
from bs4 import BeautifulSoup
from time import monotonic

start = monotonic()
base_url = 'https://parsinger.ru/asyncio/create_soup/1/'
codes = {'valid': 0}


async def get_soup(url: str, session: aiohttp.ClientSession) -> BeautifulSoup:
    async with session.get(url) as response:
        response = await response.text()
    return BeautifulSoup(response, 'lxml')


async def fetch(url: str, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> None:
    async with semaphore:
        async with session.get(url) as response:
            await response.text()
            if response.status == 200:
                soup = await get_soup(url, session)
                codes['valid'] += int(soup.select_one('.text').text)


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        semaphore = asyncio.Semaphore(10)
        soup = await get_soup(base_url + 'index.html', session)
        links = [base_url + link['href'] for link in soup.find_all('a')]
        await asyncio.gather(*[asyncio.create_task(fetch(link, session, semaphore)) for link in links])


if __name__ == '__main__':
    asyncio.run(main())
    print(codes)
    print('Executing time:', monotonic() - start)
