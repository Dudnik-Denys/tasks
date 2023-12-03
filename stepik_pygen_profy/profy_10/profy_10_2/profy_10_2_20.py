def filterfalse(predicate, iterable):
    predicate = bool if predicate is None else predicate
    return filter(lambda x: not predicate(x), iterable)
