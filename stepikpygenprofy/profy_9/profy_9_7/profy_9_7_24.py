def takes_positive(func):
    def wrapper(*args, **kwargs):
        for elem in args:
            if type(elem) is not int:
                raise TypeError
            if elem <= 0:
                raise ValueError

        for value in kwargs.values():
            if type(value) is not int:
                raise TypeError
            if value <= 0:
                raise ValueError

        result = func(*args, **kwargs)
        return result
    return wrapper
