def intersperse(iterable, delimiter):
    iterable = iter(iterable)
    try:
        yield next(iterable)
    except StopIteration:
        return
    for elem in iterable:
        yield delimiter
        yield elem
