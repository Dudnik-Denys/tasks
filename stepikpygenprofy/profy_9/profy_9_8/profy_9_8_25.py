from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    result = func(*args, **kwargs)
                except Exception:
                    pass
                else:
                    break
            try:
                return result
            except:
                raise MaxRetriesException
        return wrapper
    return decorator


@retry(99)
def calculate(a, b, c):
    """Calculate something"""
    calculate.calls = calculate.__dict__.get('calls', 0) + 1
    if calculate.calls < 4:
        raise ValueError
    return a + b + c

print(calculate.__name__)
print(calculate.__doc__)
try:
    print(calculate(2000, b=1, c=4))
except Exception as e:
    print(type(e))