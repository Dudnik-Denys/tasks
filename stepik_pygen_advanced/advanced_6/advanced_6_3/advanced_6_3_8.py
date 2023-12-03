num_1, num_2, num_3 = int(input()), int(input()), int(input())


def parabola(a: int, b: int, c: int) -> tuple:
    result = (-b / (a * 2), ((4 * a * c) - b ** 2) / (4 * a))
    return result


print(parabola(num_1, num_2, num_3))
