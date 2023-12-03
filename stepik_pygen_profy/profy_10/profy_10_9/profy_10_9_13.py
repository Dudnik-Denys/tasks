from itertools import dropwhile


def drop_this(iterable, obj):
    return dropwhile(lambda x: x == obj, iterable)
