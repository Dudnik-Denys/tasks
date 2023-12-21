class Rectangle:
    def __init__(self, length, width):
        self.length, self.width = length, width

    def __repr__(self):
        return f'Rectangle({self.length}, {self.width})'
