from functools import wraps


def strip_range(start: int, end: int, char: str = '.'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            char_nums = end - start if end < len(result) else len(result) - start
            return f'{result[:start]}{char * char_nums}{result[end:]}'
        return wrapper
    return decorator
