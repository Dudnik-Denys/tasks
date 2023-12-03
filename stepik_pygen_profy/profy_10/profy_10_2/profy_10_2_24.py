from copy import copy


def get_min_max(iterable):
    try:
        minimum = min(copy(iterable))
        maximum = max(copy(iterable))
        return minimum, maximum
    except ValueError:
        return None
