class WriteSpy:
    def __init__(self, file1, file2, to_close: bool = False):
        self._modes = ['w', 'x', 'r+', 'a', 'a+']
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.close()

    def write(self, text):
        if not self.writable():
            raise ValueError('Файл закрыт или недоступен для записи')
        self.file1.write(text)
        self.file2.write(text)

    def closed(self):
        return self.file1.closed and self.file2.closed

    def writable(self):
        return self.file1.mode in self._modes and self.file2.mode in self._modes and not self.file1.closed and not \
               self.file2.closed

    def close(self):
        self.file1.close()
        self.file2.close()
