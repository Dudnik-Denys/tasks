from typing import Iterable
from itertools import islice


def take(iterable: Iterable, n: int) -> Iterable:
    return islice(iterable, n)
