class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{type(self).__name__}({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self.__add__(other)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __truediv__(self, other):
        if type(other) in (int, float):
            return Vector(self.x / other, self.y / other)
        return NotImplemented

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)
