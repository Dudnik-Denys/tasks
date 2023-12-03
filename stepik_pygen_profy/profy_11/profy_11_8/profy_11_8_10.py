import re


def normalize_whitespace(string: str) -> str:
    result = re.sub(r'\s+', ' ', string)
    return result


print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))
