from itertools import accumulate
from operator import mul


def factorials(n):
    return accumulate(range(1, n + 1), mul)
