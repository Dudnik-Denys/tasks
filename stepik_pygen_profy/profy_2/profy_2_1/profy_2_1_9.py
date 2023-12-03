def convert(string: str) -> str:
    cnt_lower = 0
    cnt_upper = 0
    for symbol in string:
        if symbol.isalpha() and symbol.islower():
            cnt_lower += 1
        if symbol.isalpha() and symbol.isupper():
            cnt_upper += 1

    return string.lower() if cnt_lower >= cnt_upper else string.upper()


print(convert('ABCdef'))
