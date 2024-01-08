class MutableString:
    def __init__(self, string: str = ''):
        self.string = string

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"{type(self).__name__}('{self.string}')"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        yield from self.string

    def __getitem__(self, item):
        if isinstance(item, int | slice):
            return MutableString(self.string[item])

    def __setitem__(self, key, value):
        if isinstance(key, int | slice):
            temp = list(self.string)
            temp[key] = value
            self.string = ''.join(temp)

    def __delitem__(self, key):
        if isinstance(key, int | slice):
            temp = list(self.string)
            del temp[key]
            self.string = ''.join(temp)

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()x
