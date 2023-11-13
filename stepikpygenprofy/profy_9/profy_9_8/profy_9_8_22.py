from functools import wraps


def takes(*elems):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            common = list(args)

            if len(kwargs.values()) > 0:
                for value in kwargs.values():
                    common.append(value)

            for elem in common:
                if not isinstance(elem, elems):
                    raise TypeError

            result = func(*args, **kwargs)

            return result
        return wrapper
    return decorator
