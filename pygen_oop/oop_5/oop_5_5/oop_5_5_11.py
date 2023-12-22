class SuperString:
    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if type(other) == int:
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) == int:
            limit = len(self.string) // other
            return SuperString(self.string[:limit])
        return NotImplemented

    def __lshift__(self, other):
        if type(other) == int:
            if other < len(self.string):
                limit = len(self.string) - other
                return SuperString(self.string[:limit])
            return SuperString('')
        return NotImplemented

    def __rshift__(self, other):
        if type(other) == int:
            if other < len(self.string):
                return SuperString(self.string[other:])
            return SuperString('')
        return NotImplemented
