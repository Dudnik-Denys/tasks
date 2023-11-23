from itertools import pairwise


def is_rising(iterable):
    return all(first < second for first, second in pairwise(iterable))
