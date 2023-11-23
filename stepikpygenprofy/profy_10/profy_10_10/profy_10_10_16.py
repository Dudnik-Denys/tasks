from itertools import chain
from itertools import tee


def ncycles(iterable, times):
    return chain.from_iterable(tee(iterable, times))
