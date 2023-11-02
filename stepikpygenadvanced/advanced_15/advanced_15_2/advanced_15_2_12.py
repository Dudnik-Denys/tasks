def mean(*args):
    length = len([num for num in args if type(num) in (int, float)])
    total = sum([num for num in args if type(num) in (int, float)])
    if length == 0:
        return 0.0
    return total / length
