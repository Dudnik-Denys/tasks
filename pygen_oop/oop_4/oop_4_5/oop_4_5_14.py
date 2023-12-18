class HourClock:
    def __init__(self, hours):
        self.hours = hours

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if type(value) == int and value in range(1, 13):
            self._hours = value
        else:
            raise ValueError('Некорректное время')
