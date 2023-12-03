from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}")
        if isinstance(result, str):
            print(f"TRACE: возвращаемое значение {func.__name__}(): '{result}'")
        else:
            print(f"TRACE: возвращаемое значение {func.__name__}(): {result}")
        return result
    return wrapper
