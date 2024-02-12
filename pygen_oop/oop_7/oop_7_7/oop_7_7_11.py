from datetime import date


class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def iso_format(self):
        return date(self.year, self.month, self.day).isoformat()

    def format(self):
        return date.fromisoformat(self.iso_format()).strftime('%m-%d-%Y')


class ItalianDate(USADate):
    def format(self):
        return date.fromisoformat(self.iso_format()).strftime('%d/%m/%Y')
