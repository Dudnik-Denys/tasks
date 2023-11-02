def choose_plural(amount: int, declensions: tuple):
    last = str(amount)[-1]
    if len(str(amount)) == 1:
        if last in '1':
            return f'{amount} {declensions[0]}'
        elif last in '234':
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'
    elif len(str(amount)) > 1 and int(str(amount)[-2:]) not in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
        if last in '1':
            return f'{amount} {declensions[0]}'
        elif last in '234':
            return f'{amount} {declensions[1]}'
        else:
            return f'{amount} {declensions[2]}'
    else:
        return f'{amount} {declensions[2]}'
