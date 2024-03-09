from string import ascii_lowercase, digits
import re


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits
    CARD_PATTERN = re.compile(r'\d{4}-\d{4}-\d{4}-\d{4}')
    NAME_PATTERN = re.compile(r'[A-Z0-9]+\s[A-Z0-9]+')

    @staticmethod
    def check_card_number(number):
        return True if re.fullmatch(CardCheck.CARD_PATTERN, number) is not None else False

    @staticmethod
    def check_name(name):
        return True if re.fullmatch(CardCheck.NAME_PATTERN, name) is not None else False
