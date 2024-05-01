import asyncio
import aiohttp
from bs4 import BeautifulSoup
from time import monotonic

start_time = monotonic()
base_url = 'https://asyncio.ru/zadachi/3/'


async def get_soup(url: str, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> BeautifulSoup:
    async with semaphore:
        async with session.get(url) as response:
            return BeautifulSoup(await response.text(), 'lxml')


async def main():
    semaphore = asyncio.Semaphore(5)
    async with aiohttp.ClientSession() as session:
        links = []
        main_soup = await get_soup(base_url + 'index.html', session, semaphore)
        depth_1 = [base_url + link['href'] for link in main_soup.select('a')]
        depth_1_soups = await asyncio.gather(*[asyncio.create_task(get_soup(url, session, semaphore)) for url in depth_1])
        [links.extend(soup.select('a')) for soup in depth_1_soups]
        links = [base_url + 'depth1/' + link['href'] for link in links]
        depth_2_soups = await asyncio.gather(*[asyncio.create_task(get_soup(url, session, semaphore)) for url in links])
        return sum([int(soup.select_one('#number').text) for soup in depth_2_soups])


if __name__ == '__main__':
    print(asyncio.run(main()))
