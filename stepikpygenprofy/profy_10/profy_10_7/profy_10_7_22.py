def pairwise(iterable):
    iterator = iter(iterable)
    if iterable:
        next_elem = None
        curr_elem = next(iterator)
        while True:
            try:
                next_elem = next(iterator)
                yield curr_elem, next_elem
                curr_elem = next_elem
            except StopIteration:
                yield curr_elem, None
                return StopIteration
    else:
        return iterable
