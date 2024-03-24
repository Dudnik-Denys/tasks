import asyncio

# Список заклинаний с временем каста
spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Вихрь ветра": 5,
    "Лечебное зелье": 1,
    "Призыв зверя": 6,
    "Невидимость": 4,
    "Защитный барьер": 3,
    "Телепортация": 7,
    "Призыв дождя": 2,
}

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]


async def cast_spell(student: str, spell: str, cast_time: int | float) -> None:
    try:
        await asyncio.sleep(cast_time)
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    except asyncio.CancelledError:
        await asyncio.sleep(cast_time - max_cast_time)
        print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. "
              f"{student} успешно завершает заклинание с помощью shield.")


async def main() -> None:
    tasks = [asyncio.shield(asyncio.create_task(cast_spell(student, spell, cast)))
             for student in students for spell, cast in spells.items()]

    try:
        await asyncio.wait_for(asyncio.gather(*tasks), max_cast_time)
    except asyncio.TimeoutError:
        pass


asyncio.run(main())
