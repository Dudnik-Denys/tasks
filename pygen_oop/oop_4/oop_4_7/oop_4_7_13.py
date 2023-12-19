from typing import Iterable


class QuadraticPolynomial:
    def __init__(self, a: int | float, b: int | float, c: int | float):
        self.a, self.b, self.c = a, b, c

    @classmethod
    def from_iterable(cls, data: Iterable[int | float]):
        return QuadraticPolynomial(*data)

    @classmethod
    def from_str(cls, data: str):
        return QuadraticPolynomial(*map(float, data.split()))
