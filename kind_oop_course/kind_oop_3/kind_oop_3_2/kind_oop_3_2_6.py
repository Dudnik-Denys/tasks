class DigitRetrieve:
    def __call__(self, value):
        try:
            return int(value)
        except ValueError:
            return None
