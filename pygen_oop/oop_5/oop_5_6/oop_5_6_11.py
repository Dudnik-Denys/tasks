from random import choice


class Dice:
    def __init__(self, sides: int):
        self.sides = sides

    def __call__(self):
        return choice(range(1, self.sides + 1))
