from contextlib import contextmanager


@contextmanager
def make_tag(tag: str):
    print(tag)
    yield
    print(tag)
