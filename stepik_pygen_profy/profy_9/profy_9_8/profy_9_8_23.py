from functools import wraps


def add_attrs(**attrs):
    def decorator(func):
        for key, value in attrs.items():
            func.__dict__[key] = value

        @wraps(func)
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
