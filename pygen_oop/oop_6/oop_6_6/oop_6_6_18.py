from contextlib import contextmanager
import sys


@contextmanager
def reversed_print():
    default_write = sys.stdout.write
    sys.stdout.write = lambda text: default_write(text[::-1])
    yield
    sys.stdout.write = default_write
