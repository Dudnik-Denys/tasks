from functools import wraps


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if not isinstance(result, str):
            raise TypeError

        return result
    return wrapper
