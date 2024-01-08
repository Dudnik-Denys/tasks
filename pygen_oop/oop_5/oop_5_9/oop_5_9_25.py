from itertools import cycle
from typing import Callable


def limited_hash(left: int, right: int, hash_function: Callable = hash):
    def new_func(obj):
        result = hash_function(obj)
        if result in range(left, right + 1):
            return result
        if result > right:
            diff = abs(result - right)
            elem = left
            seq = cycle(range(left, right + 1))
            while diff:
                elem = next(seq)
                diff -= 1
            return elem
        if result < left:
            diff = abs(left - result)
            elem = right
            seq = cycle(range(right, left - 1, -1))
            while diff:
                elem = next(seq)
                diff -= 1
            return elem

    return new_func


# Гениальное решение
# def limited_hash(left, right, hash_function=hash):
#     def inner_hash_function(x):
#         return left + (hash_function(x) - left) % (right - left + 1)
#     return inner_hash_function
