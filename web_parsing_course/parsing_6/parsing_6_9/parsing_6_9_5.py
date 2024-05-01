import asyncio
import aiohttp
import aiofiles
import os
from bs4 import BeautifulSoup

base_url = 'https://parsinger.ru/asyncio/aiofile/2/'


async def get_soup(url: str, session: aiohttp.ClientSession) -> BeautifulSoup:
    async with session.get(url) as response:
        response = await response.text()
    return BeautifulSoup(response, 'lxml')


async def get_images_links(pages: list, session: aiohttp.ClientSession) -> list:
    result = []
    for page in pages:
        soup = await get_soup(base_url + page, session)
        links = [link['src'] for link in soup.find_all('img')]
        for link in links:
            if link not in result:
                result.append(link)
    return result


async def download_file(link: str, session: aiohttp.ClientSession) -> None:
    img_name = link.split('/')[-1]
    async with aiofiles.open(f'images/{img_name}', 'wb') as file:
        async with session.get(link) as response:
            async for chunk in response.content.iter_chunked(1024):
                await file.write(chunk)


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        soup = await get_soup(base_url + 'index.html', session)
        pages = [link['href'] for link in soup.find_all('a')]
        links = await get_images_links(pages, session)
        await asyncio.gather(*[asyncio.create_task(download_file(link, session)) for link in links])


def get_folder_size(filepath: str, size=0) -> int | float:
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


if __name__ == '__main__':
    asyncio.run(main())
    images_size = get_folder_size('images/')
    print(images_size)
