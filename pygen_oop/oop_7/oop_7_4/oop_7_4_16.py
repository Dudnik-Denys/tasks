class DefaultList(list):
    def __init__(self, iterable=None, default=None):
        if iterable:
            super().__init__(item for item in iterable)
        self.default = default

    def __setitem__(self, index, item):
        super().__setitem__(index, item)

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except IndexError:
            return self.default

    def insert(self, index, item):
        super().insert(index, item)

    def append(self, item):
        super().append(item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(item for item in other)
