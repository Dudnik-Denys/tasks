from functools import wraps


def make_html(tag: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return decorator
