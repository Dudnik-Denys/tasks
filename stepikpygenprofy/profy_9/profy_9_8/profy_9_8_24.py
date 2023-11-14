from functools import wraps


def ignore_exception(*errors):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except errors as error:
                print(f'Исключение {type(error).__name__} обработано')
            else:
                return result
        return wrapper
    return decorator
