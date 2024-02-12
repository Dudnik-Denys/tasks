from collections.abc import Iterator, Iterable


def is_iterator(obj):
    return isinstance(obj, Iterator)


def is_iterable(obj):
    return isinstance(obj, Iterable)
