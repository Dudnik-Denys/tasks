from itertools import count


def tabulate(func):
    return map(func, count(1))
