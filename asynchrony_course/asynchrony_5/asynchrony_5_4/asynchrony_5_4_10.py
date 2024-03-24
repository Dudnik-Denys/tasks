import asyncio

places = [
   "начинает путешествие",
   "находит загадочный лес",
   "переправляется через реку",
   "встречает дружелюбного дракона",
   "находит сокровище"]

roles = ["Искатель приключений", "Храбрый рыцарь", "Отважный пират"]


async def counter(name: str, delay: int | float) -> None:
    for place in places:
        print(name, place + '...')
        await asyncio.sleep(delay)


async def main():
    await asyncio.gather(*[asyncio.create_task(counter(hero, 1)) for hero in roles])


asyncio.run(main())
