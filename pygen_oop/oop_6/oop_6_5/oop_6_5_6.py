class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self

    def __exit__(self, *args, **kwargs):
        print(f'До встречи, {self.name}!')
