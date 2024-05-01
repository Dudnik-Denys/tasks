import asyncio
import aiohttp
import aiofiles
import os
from bs4 import BeautifulSoup
from time import monotonic
from aiohttp import TCPConnector

start_time = monotonic()
base_url = 'https://parsinger.ru/asyncio/aiofile/3/'
data = {'categories': [],
        'pages': [],
        'images': []}


def get_folder_size(filepath: str, size=0) -> int | float:
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


async def get_soup(url: str, session: aiohttp.ClientSession) -> BeautifulSoup:
    async with session.get(url) as response:
        response = await response.text()
    return BeautifulSoup(response, 'lxml')


async def get_categories(url: str, session: aiohttp.ClientSession) -> None:
    soup = await get_soup(url, session)
    print('categories list extended')
    data['categories'] = [base_url + link['href'] for link in soup.find_all('a')]


async def get_pages(url: str, session: aiohttp.ClientSession) -> None:
    soup = await get_soup(url, session)
    print('pages list extended')
    data['pages'].extend([base_url + 'depth2/' + link['href'] for link in soup.find_all('a')])


async def get_images(url: str, session: aiohttp.ClientSession) -> None:
    soup = await get_soup(url, session)
    for link in soup.find_all('img'):
        if link['src'] not in data['images']:
            data['images'].append(link['src'])
            print('images list extended')


async def download_file(url: str, session: aiohttp.ClientSession, locker: asyncio.Semaphore) -> None:
    file_name = url.split('/')[-1]
    async with locker:
        async with aiofiles.open(f'images/{file_name}', 'wb') as file:
            async with session.get(url) as response:
                async for chunk in response.content.iter_chunked(1024):
                    await file.write(chunk)

    print(f"Downloaded {file_name}")


async def main() -> None:
    connector = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=connector) as session:
        semaphore = asyncio.Semaphore(10)
        await get_categories(base_url + 'index.html', session)
        await asyncio.gather(*[asyncio.create_task(get_pages(category, session)) for category in data['categories']])
        await asyncio.gather(*[asyncio.create_task(get_images(page, session)) for page in data['pages']])
        await asyncio.gather(*[asyncio.create_task(download_file(image, session, semaphore)) for image in data['images']])
        print(data['images'])


if __name__ == '__main__':
    asyncio.run(main())
    images_size = get_folder_size('images/')
    print('Executing time:', monotonic() - start_time)
