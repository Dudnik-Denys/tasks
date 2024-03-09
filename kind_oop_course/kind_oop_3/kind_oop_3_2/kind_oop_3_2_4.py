class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = extensions

    def __call__(self, filename):
        for extension in self.extensions:
            if filename.endswith(f'.{extension}'):
                return True
        return False
