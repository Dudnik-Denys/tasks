import time


def calculate_it(func, value):
    start = time.perf_counter()
    func(value)
    finish = time.perf_counter()
    return finish - start


def get_the_fastest_func(funcs: list, arg):
    speed = {}

    for func in funcs:
        t = calculate_it(func, arg)
        speed[t] = func

    return speed[min(speed)]
