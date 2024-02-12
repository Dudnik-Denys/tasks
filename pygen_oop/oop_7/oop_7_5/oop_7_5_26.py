class SortedList:
    def __init__(self, iterable=None):
        self._iterable = sorted(iterable) if iterable else []

    def append(self, obj):
        raise NotImplementedError

    def extend(self, obj):
        raise NotImplementedError

    def insert(self, index, obj):
        raise NotImplementedError

    def reverse(self):
        raise NotImplementedError

    def __repr__(self):
        return f'{type(self).__name__}({str(self._iterable)})'

    def __reversed__(self):
        raise NotImplementedError

    def __len__(self):
        return len(self._iterable)

    def __iter__(self):
        yield from self._iterable

    def __contains__(self, item):
        return item in self._iterable

    def __getitem__(self, item):
        return self._iterable[item]

    def __delitem__(self, key):
        del self._iterable[key]

    def __setitem__(self, key, value):
        raise NotImplementedError

    def add(self, obj):
        self._iterable.append(obj)
        self._iterable = sorted(self._iterable)

    def discard(self, obj):
        while obj in self._iterable:
            self._iterable.remove(obj)
        self._iterable = sorted(self._iterable)

    def update(self, iterable):
        self._iterable.extend(iterable)
        self._iterable = sorted(self._iterable)

    def __add__(self, other):
        if isinstance(other, SortedList):
            return SortedList(self._iterable + other._iterable)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self._iterable = sorted(self._iterable + other._iterable)
            return self
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SortedList(self._iterable * other)
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int):
            self._iterable = sorted(self._iterable * other)
            return self
        return NotImplemented
