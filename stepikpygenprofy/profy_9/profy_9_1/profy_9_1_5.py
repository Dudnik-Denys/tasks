def convert(number: int, indent=2, minus='') -> tuple:
    if number < 0:
        indent = 3
        minus = '-'
    return f'{minus}{bin(number)[indent:]}', f'{minus}{oct(number)[indent:]}', f'{minus}{hex(number)[indent:].upper()}'
