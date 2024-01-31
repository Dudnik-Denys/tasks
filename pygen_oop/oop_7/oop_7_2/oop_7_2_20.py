class Summator:
    @staticmethod
    def total(num, power=1):
        if num < 0:
            return ValueError('Число должно быть больше нуля')

        result = 0

        for n in range(num, -1, -1):
            result += (n ** power)

        return result


class SquareSummator(Summator):
    def total(self, num, power=2):
        return super().total(num, power)


class QubeSummator(Summator):
    def total(self, num, power=3):
        return super().total(num, power)


class CustomSummator(Summator):
    def __init__(self, power):
        self.power = power

    def total(self, num):
        return super().total(num, self.power)
