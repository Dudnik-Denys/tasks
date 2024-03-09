from random import choice
from string import ascii_lowercase, ascii_uppercase, digits


class EmailValidator:
    SYMBOLS = ascii_lowercase + ascii_uppercase + digits + '_' + '.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        length = choice(range(3, 101))
        first_half = ''
        second_half = '@'

        for char in range(length):
            if len(first_half) > 0 and first_half[-1] != '.':
                elem = choice(cls.SYMBOLS)
            else:
                elem = choice(cls.SYMBOLS[:-1])
            first_half += elem

        length = choice(range(3, 51))

        for char in range(length):
            if second_half[-1] != '.':
                elem = choice(cls.SYMBOLS)
            else:
                elem = choice(cls.SYMBOLS[:-1])
            second_half += elem

        new_str = ''

        if '.' not in second_half:
            mid_len = len(second_half) // 2
            new_str = second_half[:mid_len] + '.' + second_half[mid_len:]

        email = first_half + second_half if '.' in second_half else first_half + new_str

        return email

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email) and email.count('@') == 1 and '..' not in email:
            first_half, second_half = email.split('@')
            if 0 < len(first_half) <= 100 and 3 < len(second_half) <= 50 and second_half.count('.') >= 1:
                for char in first_half:
                    if char not in cls.SYMBOLS:
                        return False
                for char in second_half:
                    if char not in cls.SYMBOLS:
                        return False
                return True
        return False

    @staticmethod
    def __is_email_str(email):
        return isinstance(email, str)
