class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except AttributeError:
            print('Незакрываемый объект')
