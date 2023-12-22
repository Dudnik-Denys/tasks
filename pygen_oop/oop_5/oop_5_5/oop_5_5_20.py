class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value % 24

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        hours = value // 60
        minutes = value - (60 * hours)
        self._minutes = minutes
        self._hours += hours

    def __str__(self):
        return f'{self._hours if self._hours > 9 else f"0{self._hours}"}:' \
               f'{self._minutes if self._minutes > 9 else f"0{self._minutes}"}'

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self._hours + other._hours, self._minutes + other._minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours += other._hours
            self.minutes += other._minutes
            return self
        return NotImplemented
