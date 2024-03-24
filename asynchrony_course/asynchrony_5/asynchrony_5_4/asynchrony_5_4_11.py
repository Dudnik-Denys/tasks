import asyncio


async def countdown(name, seconds):
    text = 'Найди скрытые сокровища!' if name == 'Квест на поиск сокровищ' else 'Беги быстрее, дракон на хвосте!'
    for i in range(seconds):
        print(f'{name}: Осталось {seconds - i} сек. {text}')
        await asyncio.sleep(1)
    print(f'{name}: Задание выполнено! Что дальше?')


async def main():
    treasure_hunt = asyncio.create_task(countdown('Квест на поиск сокровищ', 10))
    dragon_escape = asyncio.create_task(countdown('Побег от дракона', 5))
    await asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())
