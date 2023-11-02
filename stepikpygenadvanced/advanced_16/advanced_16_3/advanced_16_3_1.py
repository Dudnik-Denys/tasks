def concat(*args, sep=' '):
    args = [str(symb) for symb in args]
    return f'{sep}'.join(args)
