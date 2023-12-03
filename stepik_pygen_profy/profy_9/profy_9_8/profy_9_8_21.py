from functools import wraps


def returns(datatype: type):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, datatype):
                raise TypeError
            return result
        return wrapper
    return decorator
