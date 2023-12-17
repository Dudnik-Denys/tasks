class Scales:
    def __init__(self):
        self.left = 0
        self.right = 0

    def add_right(self, mass):
        self.right += mass

    def add_left(self, mass):
        self.left += mass

    def get_result(self):
        return ['Левая чаша тяжелее', 'Правая чаша тяжелее'][self.right > self.left] \
            if self.left != self.right else 'Весы в равновесии'
