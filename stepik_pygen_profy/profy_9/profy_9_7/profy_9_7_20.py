def decor(func):
    def wrapper(*args, **kwargs):
        args = (i.upper() if isinstance(i, str) else i for i in args)
        kwargs = {k: v.upper() if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapper


print = decor(print)
