from functools import reduce
from operator import mul


def product_of_odds(data):
    return reduce(mul, filter(lambda x: x % 2 == 1, data), 1)
