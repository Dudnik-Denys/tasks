class OrderedSet:
    def __init__(self, iterable=()):
        self._data = dict.fromkeys(iterable, None)

    def __len__(self):
        return len(self._data)

    def add(self, item):
        self._data.setdefault(item, None)

    def discard(self, item):
        self._data.pop(item, None)

    def __iter__(self):
        yield from self._data

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self._data) == len(other._data) and all(x == y for x, y in zip(self._data, other._data))
        if isinstance(other, set):
            return set(self._data) == other
        return NotImplemented
