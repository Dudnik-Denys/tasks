from random import choice, randint


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []

for _ in range(217):
    name = choice(['Line', 'Rect', 'Ellipse'])
    obj = eval(f'{name}({randint(0, 100)}, {randint(0, 100)}, {randint(0, 100)}, {randint(0, 100)})')
    elements.append(obj)

for elem in elements:
    if isinstance(elem, Line):
        elem.sp = (0, 0)
        elem.ep = (0, 0)
