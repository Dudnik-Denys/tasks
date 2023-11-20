def all_together(*args):
    for arg in args:
        yield from arg

