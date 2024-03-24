import asyncio

runners = {
    "Молния Марк": 12.8,
    "Ветренный Виктор": 13.5,
    "Скоростной Степан": 11.1,
    "Быстрая Белла": 10.8,
    "Легкая Лиза": 11.3,
    "Ракетный Роман": 9.8,
    "Турбо Таня": 13.7,
    "Живчик Женя": 12.5,
    "Вихревой Валерий": 14.5,
    "Газель Галина": 13.4,
    "Непобедимый Никита": 11.7,
    "Прыгун Павел": 10.9,
    "Зефирный Захар": 11.2,
    "Метеор Марина": 9.3,
    "Экспресс Елена": 9.1,
    "Флеш Филипп": 10.2,
    "Аэродинамичная Алина": 8.6,
    "Бриз Борис": 9.4,
    "Ветерок Василий": 13.1,
    "Стрела Станислав": 12.9
}


async def run_lap(name: str, speed: int | float):
    result = round(100 / speed, 2)
    await asyncio.sleep(result)
    print(f"{name} завершил круг за {result} секунд")


async def main(max_time=10):
    tasks = [asyncio.wait_for(run_lap(name, speed), max_time) for name, speed in runners.items()]
    try:
        await asyncio.gather(*tasks)
    except asyncio.TimeoutError:
        pass


asyncio.run(main())
