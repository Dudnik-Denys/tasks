import asyncio
import aiohttp
from bs4 import BeautifulSoup
from time import monotonic

start = monotonic()


class Parser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.start_category = 'index1_page_1.html'
        self.items_total_sale = 0

    @staticmethod
    async def get_soup(url: str, session: aiohttp.ClientSession) -> BeautifulSoup:
        async with session.get(url) as response:
            response = await response.text()
        return BeautifulSoup(response, 'lxml')

    async def get_pages(self, category_url: str, session: aiohttp.ClientSession) -> list:
        async with session.get(self.base_url + category_url) as response:
            response = await response.text()
            soup = BeautifulSoup(response, 'lxml')
            pages = [link['href'] for link in soup.select_one('.pagen').select('a')]
        return pages

    async def get_categories(self, session: aiohttp.ClientSession) -> list:
        async with session.get(self.base_url + self.start_category) as response:
            response = await response.text()
            soup = BeautifulSoup(response, 'lxml')
            categories = [link['href'] for link in soup.select_one('.nav_menu').select('a')]
        return categories

    async def get_items(self, page_url: str, session: aiohttp.ClientSession) -> list:
        async with session.get(self.base_url + page_url) as response:
            response = await response.text()
            soup = BeautifulSoup(response, 'lxml')
            items = [link['href'] for link in soup.select('.name_item[href]')]
        return items

    async def get_data(self, item_url: str, session: aiohttp.ClientSession) -> None:
        async with session.get(self.base_url + item_url) as response:
            response = await response.text()
            soup = BeautifulSoup(response, 'lxml')
            price = soup.select_one('#price').text.split()[0]
            old_price = soup.select_one('#old_price').text.split()[0]
            in_stock =  soup.select_one('#in_stock').text.split(': ')[-1]
            self.items_total_sale += (int(old_price) - int(price)) * int(in_stock)

    async def run_parser(self) -> None:
        async with aiohttp.ClientSession() as session:
            categories = await self.get_categories(session)
            for category in categories:
                pages = await self.get_pages(category, session)
                for page in pages:
                    items = await self.get_items(page, session)
                    await asyncio.gather(*[asyncio.create_task(self.get_data(item, session)) for item in items])


if __name__ == '__main__':
    parser = Parser('https://parsinger.ru/html/')
    asyncio.run(parser.run_parser())
    print(parser.items_total_sale)
    print('Executing time:', monotonic() - start)
