from itertools import islice


def take_nth(iterable, n):
    return next(islice(iterable, n - 1, n), None)
