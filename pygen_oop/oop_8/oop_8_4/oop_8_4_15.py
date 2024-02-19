from functools import wraps


class ignore_exception:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exception:
                if type(exception) not in self.exceptions:
                    raise exception
                print(f'Исключение {type(exception).__name__} обработано')
        return wrapper
