class ListMath:
    def __init__(self, data=None):
        self.lst_math = [elem for elem in data if type(elem) in (int, float)] if data is not None else []

    def __add__(self, other):
        if type(other) in (int, float):
            return ListMath([elem + other for elem in self.lst_math])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if type(other) in (int, float):
            return ListMath([elem - other for elem in self.lst_math])

    def __rsub__(self, other):
        if type(other) in (int, float):
            return ListMath([other - elem for elem in self.lst_math])

    def __mul__(self, other):
        if type(other) in (int, float):
            return ListMath([elem * other for elem in self.lst_math])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in (int, float):
            return ListMath([elem / other for elem in self.lst_math])

    def __rtruediv__(self, other):
        if type(other) in (int, float):
            return ListMath([other / elem for elem in self.lst_math])

    def __iadd__(self, other):
        if type(other) in (int, float):
            for i in range(len(self.lst_math)):
                self.lst_math[i] += other
        return self

    def __isub__(self, other):
        if type(other) in (int, float):
            for i in range(len(self.lst_math)):
                self.lst_math[i] -= other
        return self

    def __imul__(self, other):
        if type(other) in (int, float):
            for i in range(len(self.lst_math)):
                self.lst_math[i] *= other
        return self

    def __itruediv__(self, other):
        if type(other) in (int, float):
            for i in range(len(self.lst_math)):
                self.lst_math[i] /= other
        return self
