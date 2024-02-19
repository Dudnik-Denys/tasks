import functools


class type_check:
    def __init__(self, types):
        self.types = types

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, self.types):
                if not isinstance(arg, arg_type):
                    raise TypeError
            value = func(*args, **kwargs)
            return value

        return wrapper
