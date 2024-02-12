from enum import Enum
from datetime import date, timedelta

Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today: date, weekday: Weekday, after_today: bool = False):
        self.after_today = after_today
        self.today = today
        self.weekday = weekday

    def date(self):
        return self.today + timedelta(days=self._different(self.weekday.value, self.today.weekday(), self.after_today))

    def days_until(self):
        return self._different(self.weekday.value, self.today.weekday(), self.after_today)

    @staticmethod
    def _different(weekday: int, curr_day: int, after: bool):
        if weekday == curr_day:
            diff = 0 if after else 7
        else:
            diff = 7 - abs(weekday - curr_day) if weekday < curr_day else abs(weekday - curr_day)
        return diff
