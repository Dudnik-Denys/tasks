def print_given(*args, **kwargs):
    for arg in args:
        print(arg, type(arg))

    for key, value in sorted(kwargs.items()):
        print(f'{key} {value} {type(value)}')
