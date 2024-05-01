import asyncio
import aiohttp
from bs4 import BeautifulSoup
from time import monotonic

start_time = monotonic()
base_url = 'https://asyncio.ru/zadachi/1/index.html'
code_dict = {
    '0': 'F',
    '1': 'B',
    '2': 'D',
    '3': 'J',
    '4': 'E',
    '5': 'C',
    '6': 'H',
    '7': 'G',
    '8': 'A',
    '9': 'I'
}


async def get_soup(url: str, session: aiohttp.ClientSession) -> BeautifulSoup:
    async with session.get(url) as response:
        return BeautifulSoup(await response.text(), 'lxml')


async def decode(text: str) -> str:
    for num, char in code_dict.items():
        text = text.replace(num, char)
    return text


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        soup = await get_soup(base_url, session)
        data = soup.select_one('p').text.strip()
        print(await decode(data))


if __name__ == '__main__':
    asyncio.run(main())
    print('Executing time:', monotonic() - start_time)
