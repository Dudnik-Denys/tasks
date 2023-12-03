from functools import wraps


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return [f'{string}{result}', f'{result}{string}'][to_the_end]
        return wrapper
    return decorator
