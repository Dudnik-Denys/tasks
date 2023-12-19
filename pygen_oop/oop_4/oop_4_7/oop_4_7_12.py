class Rectangle:
    def __init__(self, length: int | float, width: int | float):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side: int | float):
        return Rectangle(side, side)
