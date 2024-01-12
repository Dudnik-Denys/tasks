from contextlib import contextmanager


@contextmanager
def safe_open(filename: str, mode: str = 'r'):
    try:
        file = open(filename, mode)
        yield (file, None)
    except Exception as error:
        yield (None, error)
    else:
        file.close()
