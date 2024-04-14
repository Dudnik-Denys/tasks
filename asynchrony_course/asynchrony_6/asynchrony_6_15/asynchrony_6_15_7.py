import asyncio
import json
import re

banned_words = ["bug", "error", "exception", "fail", "crash", "hang", "slow", "memory leak", "infinite loop",
                "deadlock"]

with open('task_2_message.json', encoding='utf-8') as file:
    file_data = json.load(file)


async def check_message(dct: dict) -> str:
    if dct['role'] == 'admin':
        return 'admin: ' + dct['message']
    elif dct['role'] == 'moderator':
        message = 'moderator: ' + dct['message']
        for word in banned_words:
            message = message.replace(word, '****')
        return message
    elif dct['role'] == 'student':
        if any([re.search(word, dct['message']) for word in banned_words]):
            return 'student: В сообщении есть запрещённое слово, сообщение скрыто'
        return 'student: ' + dct['message']
    elif dct['role'] == 'black_list_user':
        return 'black_list_user: Пользователь забанен, сообщение скрыто'
    return 'None: ERROR_USER_NONE'


async def main() -> None:
    tasks = [asyncio.create_task(check_message(data), name=data['role']) for data in file_data]
    await asyncio.gather(*tasks)
    [print(task.result()) for task in tasks]

asyncio.run(main())
