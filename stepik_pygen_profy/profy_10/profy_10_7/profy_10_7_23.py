def around(iterable):
    iterator = iter(iterable)
    previous = None
    current = next(iterator, None)

    while current is not None:
        future = next(iterator, None)
        yield (previous, current, future)
        previous, current = current, future
