from functools import singledispatchmethod
from datetime import date


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def date_case(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def str_case(self, birth_date):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except ValueError:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(list)
    @__init__.register(tuple)
    def list_case(self, birth_date):
        self.birth_date = date(*birth_date)

    @property
    def age(self):
        return (date.today() - self.birth_date).days // 365.2
