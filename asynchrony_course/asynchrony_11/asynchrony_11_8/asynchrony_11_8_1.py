import asyncio
import aiohttp
from time import monotonic

start_time = monotonic()
status_codes = []


async def fetch(url: str, session: aiohttp.ClientSession, semaphore: asyncio.Semaphore) -> None:
    async with semaphore:
        async with session.get(url) as response:
            await response.text()
            status_codes.append(response.status)


async def main() -> None:
    semaphore = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[asyncio.create_task(fetch(f"https://asyncio.ru/zadachi/5/{i}.html", session,
                               semaphore)) for i in range(1, 1001)])


if __name__ == "__main__":
    asyncio.run(main())
    print(sum(status_codes))
    print('Time of executing:', monotonic() - start_time)
