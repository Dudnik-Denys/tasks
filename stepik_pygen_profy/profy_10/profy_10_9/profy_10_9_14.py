def first_true(iterable, predicate):
    return next(filter(predicate, iterable), None)
