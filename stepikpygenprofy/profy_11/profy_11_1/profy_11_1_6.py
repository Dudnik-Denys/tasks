import re

data = input()
phone_pattern = r'7-\d{3}-\d{3}-\d{2}-\d{2}|8-\d{3}-\d{4}-\d{4}'


def phone_numbers(text: str, pattern: str) -> list:
    result = []
    regular = re.search(pattern, text)

    while regular:
        result.append(regular.group())
        index = regular.span()[-1]
        text = text[index:]
        regular = re.search(pattern, text)

    return result


[print(number) for number in phone_numbers(data, phone_pattern)]
