class EasyDict(dict):
    def __init__(self, items=(), **kwargs):
        super().__init__(items, **kwargs)
        for key, value in self.items():
            object.__setattr__(self, key, value)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().__setattr__(key, value)
