from typing import Iterable


class AdvancedTuple(tuple):
    def __add__(self, other):
        if isinstance(other, Iterable):
            return AdvancedTuple((*self, *other))

    def __radd__(self, other):
        if isinstance(other, Iterable):
            return AdvancedTuple((*other, *self))
