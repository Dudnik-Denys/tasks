old_print = print


def custom_print(*args, sep=' ', end=''):
    data = []
    sep, end = sep.upper(), end.upper()

    for elem in args:
        if isinstance(elem, str):
            data.append(elem.upper())
        else:
            data.append(elem)
    old_print(*data, sep=sep, end=end)


print = custom_print
