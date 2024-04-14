import asyncio

# Общий ресурс - база данных
database = []
Schritt = 0


# Функция для записи данных в базу данных
async def write_to_database(data):
    await asyncio.sleep(1)  # Имитация длительной операции записи
    global Schritt
    if Schritt == 2 or Schritt == 5:
        bonus = f", Счастливый номер! Бонус клиента = номер клиента {Schritt} * 100 == {Schritt * 100}"
        data = data + bonus
    Schritt += 1
    database.append(data)


# Асинхронная функция для обработки запросов клиентов
async def handle_request(lock, client_id):
    data = f"Data от клиента {client_id}"

    # Измените функцию
    async with lock:
        # Критический участок кода, требующий синхронизации
        await write_to_database(data)
        print(f"Data от клиента {client_id} успешно записан в базу данных")


# Создание и запуск корутин для обработки запросов от клиентов
async def main():
    tasks = []
    locker = asyncio.Lock()
    # Измените функцию

    for i in range(10):
        tasks.append(asyncio.create_task(handle_request(locker, i)))
    await asyncio.gather(*tasks)


# Запуск основной асинхронной функции
asyncio.run(main())

print(*database, sep="\n")
