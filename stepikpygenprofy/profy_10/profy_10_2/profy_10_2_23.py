def starmap(func: callable, iterable):
    return map(lambda x: func(*x), iterable)
