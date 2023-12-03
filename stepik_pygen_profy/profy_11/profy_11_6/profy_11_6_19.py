import re

text = input()
data = ['Здравствуйте', 'Доброе утро', 'Добрый день', 'Добрый вечер']


def good_message(message: str, greetings: list[str]) -> bool:
    for greet in greetings:
        if re.match(greet, message, re.I) is not None:
            return True
    return False


print(good_message(text, data))
