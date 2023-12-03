def generator_square_polynom(a: int, b: int, c: int) -> callable:
    def result(x: int) -> int:
        return a * x ** 2 + b * x + c
    return result
