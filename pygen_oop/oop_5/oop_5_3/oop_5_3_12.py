class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @property
    def fields(self):
        return self.x, self.y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.fields == other.fields
        if isinstance(other, tuple):
            return self.fields == other
        return NotImplemented
