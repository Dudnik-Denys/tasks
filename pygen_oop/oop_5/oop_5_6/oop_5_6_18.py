class SortKey:
    def __init__(self, *args):
        self.args = args

    def __call__(self, obj):
        return tuple(obj.__dict__[i] for i in self.args)
