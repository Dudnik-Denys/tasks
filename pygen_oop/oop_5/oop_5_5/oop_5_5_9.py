class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f'{type(self).__name__}({self.proteins}, {self.fats}, {self.carbohydrates})'

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(self.proteins + other.proteins, self.fats + other.fats,
                            self.carbohydrates + other.carbohydrates)
        return NotImplemented

    def __mul__(self, other):
        if type(other) in (int, float):
            return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)
        return NotImplemented

    def __truediv__(self, other):
        if type(other) in (int, float):
            return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)
        return NotImplemented

    def __floordiv__(self, other):
        if type(other) in (int, float):
            return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)
        return NotImplemented
