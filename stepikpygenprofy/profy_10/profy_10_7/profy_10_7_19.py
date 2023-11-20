from collections import Counter


def unique(iterable):
    yield from Counter(iterable)
