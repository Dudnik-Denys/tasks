class AdvancedList(list):
    def __init__(self, iterable):
        super().__init__(elem for elem in iterable)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def insert(self, index, item):
        super().insert(index, item)

    def append(self, item):
        super().append(item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(elem for elem in other)

    def join(self, separator=' '):
        return separator.join(map(str, self))

    def map(self, func):
        temp = list(map(func, self))
        self[:] = temp

    def filter(self, func):
        temp = filter(func, self)
        self[:] = temp
