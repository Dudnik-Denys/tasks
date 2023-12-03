def interleave(*args):
    for arg in zip(*args):
        yield from arg
