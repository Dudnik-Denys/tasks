class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return abs(((self.x ** 2) + (self.y ** 2)) ** .5)
