import asyncio
import json
import re

banned_words = ['ошибка', 'баг', 'отладка', 'память', 'процессор', 'компиляция', 'алгоритм', 'функция', 'база данных',
                'интерфейс']


async def check_message(message_id: int, message: str):
    status = not any([re.search(rf"{banned_word}\W", message.lower()) for banned_word in banned_words])

    if status:
        print(f'{message_id}: {message}')
    else:
        print(f'В сообщении {message_id} стоп-слово: task.done(): False')
        asyncio.current_task().cancel()


async def main():
    with open('task_1_message.json', encoding='utf-8') as file:
        tasks = [asyncio.create_task(check_message(dct['message_id'], dct['message'])) for dct in json.load(file)]

    await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == '__main__':
    asyncio.run(main())
