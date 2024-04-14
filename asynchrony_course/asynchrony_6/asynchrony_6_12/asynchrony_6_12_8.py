import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
            "Всего наилучшего!"]

data = {msg: code for code, msg in zip(codes, messages)}


def call_back(task: asyncio.Task) -> None:
    print('Код:', data[task.result()])


async def func(info: str) -> str:
    err_msg = 'Неверный код, сообщение скрыто'
    print('Сообщение:', info if data[info][-1] not in ('2', '4', '6', '8', '0', 'A', 'C', 'E') else err_msg)
    return info


async def main() -> None:
    for key in data:
        task = asyncio.create_task(func(key))
        task.add_done_callback(call_back)
        await task


asyncio.run(main())
