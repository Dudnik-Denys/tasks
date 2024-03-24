import asyncio

log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Запрос на выход", "delay": 2.0},
    {"event": "Ошибка авторизации", "delay": 2.5},
    {"event": "Успешное соединение с БД", "delay": 3.0},
    {"event": "Ошибка соединения с БД", "delay": 3.5},
    {"event": "Запрос к API", "delay": 4.0},
    {"event": "Ошибка запроса к API", "delay": 4.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0}]


async def fetch_log(event):
    name, delay = event["event"], event["delay"]
    await asyncio.sleep(event["delay"])
    print(f"Событие: '{name}' обработано с задержкой {delay} сек.")


async def main():
    await asyncio.gather(*[asyncio.create_task(fetch_log(data)) for data in log_events])


asyncio.run(main())
