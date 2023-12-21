import re


class PhoneNumber:
    PHONE_PATTERN = re.compile(r'^\d{10}$')

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone):
        phone = phone.replace(' ', '')
        if PhoneNumber.PHONE_PATTERN.fullmatch(phone) is not None:
            self._phone_number = phone

    def __repr__(self):
        return f"{type(self).__name__}('{self._phone_number}')"

    def __str__(self):
        return f'({self._phone_number[0:3]}) {self._phone_number[3:6]}-{self._phone_number[6:]}'
