class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.obj = open(self.filename, encoding='UTF-8')
        return (line.strip() for line in self.obj)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj.close()
