from itertools import chain


def sum_of_digits(iterable):
    return sum(map(int, chain.from_iterable(map(str, iterable))))
