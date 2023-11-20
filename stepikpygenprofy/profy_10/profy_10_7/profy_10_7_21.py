def with_previous(iterable):
    if iterable:
        previous = None
        for elem in iterable:
            yield elem, previous
            previous = elem
    else:
        return iterable
