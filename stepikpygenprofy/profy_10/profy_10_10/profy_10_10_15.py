from itertools import pairwise


def max_pair(iterable):
    return max(map(sum, pairwise(iterable)))
