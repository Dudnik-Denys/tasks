def is_iterator(obj) -> bool:
    return '__next__' in obj.__dir__()
