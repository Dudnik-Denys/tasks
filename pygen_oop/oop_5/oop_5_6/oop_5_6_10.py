class RaiseTo:
    def __init__(self, degree: int):
        self.degree = degree

    def __call__(self, x):
        return x ** self.degree
