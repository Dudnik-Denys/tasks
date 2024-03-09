# здесь объявите класс TriangleChecker
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        for key, value in self.__dict__.items():
            if type(value) not in (int, float) or value <= 0:
                return 1
            if (self.a + self.b) < self.c or (self.b + self.c) < self.a or (self.a + self.c) < self.b:
                return 2
        return 3


a, b, c = map(int, input().split()) # эту строчку не менять
# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран

tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
