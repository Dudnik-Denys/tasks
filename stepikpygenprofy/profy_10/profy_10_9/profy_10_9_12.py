from itertools import dropwhile


def drop_while_negative(iterable):
    return dropwhile(lambda num: num < 0, iterable)
