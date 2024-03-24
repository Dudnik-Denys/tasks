import asyncio


async def monitor_cpu(status_list):
    for status in status_list:
        await asyncio.sleep(.2)
        print(f"[{asyncio.current_task().get_name()}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{asyncio.current_task().get_name()}] Критическое состояние достигнуто. Инициируется остановка...")
            break


async def monitor_memory(status_list):
    for status in status_list:
        await asyncio.sleep(.2)
        print(f"[{asyncio.current_task().get_name()}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{asyncio.current_task().get_name()}] Критическое состояние достигнуто. Инициируется остановка...")
            break


async def monitor_disk_space(status_list):
    for status in status_list:
        await asyncio.sleep(.2)
        print(f"[{asyncio.current_task().get_name()}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{asyncio.current_task().get_name()}] Критическое состояние достигнуто. Инициируется остановка...")
            break


async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]
    cpu_task = asyncio.create_task(monitor_cpu(status_list), name='CPU')
    memory_task = asyncio.create_task(monitor_memory(status_list), name='Память')
    disk_task = asyncio.create_task(monitor_disk_space(status_list), name='Дисковое пространство')

    await asyncio.gather(cpu_task, memory_task, disk_task)


asyncio.run(main())
