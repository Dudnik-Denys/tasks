def greet(name, *args):
    if len(args) == 0:
        return f'Hello, {name}!'
    return f'Hello, {name} and ' + ' and '.join(args) + '!'
