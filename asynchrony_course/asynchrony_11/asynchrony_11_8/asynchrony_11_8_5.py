import asyncio
import aiohttp
import aiofiles
import os
from bs4 import BeautifulSoup
from time import monotonic

start = monotonic()
base_url = 'https://asyncio.ru/zadachi/4/'


def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


async def get_soup(url: str, session: aiohttp.ClientSession) -> BeautifulSoup:
    async with session.get(url) as response:
        return BeautifulSoup(await response.text(), 'lxml')


async def download_file(url: str, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> None:
    async with semaphore:
        file_name = url.split('/')[-1]
        async with aiofiles.open(f'images/{file_name}', 'wb') as file:
            async with session.get(url) as response:
                async for chunk in response.content.iter_chunked(1024):
                    await file.write(chunk)


async def main():
    semaphore = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        soup = await get_soup(base_url + 'index.html', session)
        links = [base_url + link['src'] for link in soup.select('img')]
        await asyncio.gather(*[asyncio.create_task(download_file(link, session, semaphore)) for link in links])


if __name__ == '__main__':
    asyncio.run(main())
    images_size = get_folder_size('images/')
    print(images_size)
    print('Executing time:', monotonic() - start)
