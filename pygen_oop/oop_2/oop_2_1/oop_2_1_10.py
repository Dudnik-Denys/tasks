def quantify(iterable, predicate):
    predicate = bool if predicate is None else predicate
    return sum(1 for elem in iterable if predicate(elem))
