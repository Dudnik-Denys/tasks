import time


def calculate_it(func, *args):
    start = time.perf_counter()
    result = func(args)
    finish = time.perf_counter()
    return result, finish - start

