class SingletonFive:
    __COUNTER = 0
    __INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if cls.__COUNTER < 5:
            cls.__COUNTER += 1
            cls.__INSTANCE = object.__new__(cls)
            return cls.__INSTANCE
        return cls.__INSTANCE

    def __init__(self, name):
        self.name = name
