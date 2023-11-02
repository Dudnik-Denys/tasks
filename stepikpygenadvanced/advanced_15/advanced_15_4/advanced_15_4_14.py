from math import sin


def math_func(num: int | float, func: str) -> int | float:
    functions = {'квадрат': num ** 2,
                 'куб': num ** 3,
                 'корень': num ** 0.5,
                 'модуль': abs(num),
                 'синус': sin(num)}
    return functions[func]


n = int(input())
s = input()
print(math_func(n, s))
