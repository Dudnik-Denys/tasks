def is_iterable(obj):
    return '__iter__' in obj.__dir__()
