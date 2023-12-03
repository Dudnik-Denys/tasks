import re


def abbreviate(phrase: str) -> str:
    result = ''
    search = re.findall(r'\B[A-Z]|\b[a-zA-Z]', phrase)
    return result.join(letter[0].upper() for letter in search)
