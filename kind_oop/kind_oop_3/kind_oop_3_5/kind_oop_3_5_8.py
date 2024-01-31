class FileAcceptor:
    def __init__(self, *extensions):
        self.extensions = extensions

    def __call__(self, filename):
        for extension in self.extensions:
            if filename.endswith(f'.{extension}'):
                return True
        return False

    def __add__(self, other):
        if isinstance(other, FileAcceptor):
            new = self.extensions + other.extensions
            return FileAcceptor(*new)
