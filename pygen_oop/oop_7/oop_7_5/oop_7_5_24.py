from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=()):
        self._iterable = iterable[:]

    def __str__(self):
        return str([elem for elem in self._iterable])

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._iterable[item]
        return NotImplemented

    def __len__(self):
        return len(self._iterable)

    def __invert__(self):
        return BitArray([0 if x == 1 else 1 for x in self._iterable])

    def __and__(self, other):
        if isinstance(other, BitArray) and len(other) == len(self):
            return BitArray([self[x] & other[x] for x in range(len(self))])
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, BitArray) and len(other) == len(self):
            return BitArray([self[x] | other[x] for x in range(len(self))])
        return NotImplemented
