import sys


class UpperPrint:
    def __enter__(self):
        self.standard_output = sys.stdout.write
        sys.stdout.write = lambda text: self.standard_output(text.upper())

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.standard_output
