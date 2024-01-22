import re


class PhoneBook:
    def __init__(self):
        self.phones = []

    def add_phone(self, phone):
        if isinstance(phone, PhoneNumber):
            self.phones.append(phone)

    def remove_phone(self, index):
        self.phones.pop(index)

    def get_phone_list(self):
        return self.phones


class PhoneNumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if re.fullmatch(r'\d{11}', str(number)) is not None:
            self._number = number

    @property
    def fio(self):
        return self._fio

    @fio.setter
    def fio(self, fio):
        if isinstance(fio, str):
            self._fio = fio
