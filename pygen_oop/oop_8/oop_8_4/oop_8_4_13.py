from functools import wraps


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_result = func(*args, **kwargs)
            if not isinstance(func_result, self.datatype):
                raise TypeError
            return func_result
        return wrapper
