class Model:
    def query(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __repr__(self):
        if self.__dict__:
            return "Model: " + ", ".join([f'{key} = {value}' for key, value in self.__dict__.items()])
        return "Model"
