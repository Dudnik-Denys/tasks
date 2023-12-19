import re


class CaseHelper:
    SNAKE_VALIDATOR = re.compile(r'([a-z]+)')
    UPPER_CAMEL_VALIDATOR = re.compile(r'([A-Z][a-z]*)')

    @staticmethod
    def is_snake(text: str) -> bool:
        return len(text.split('_')) == len(CaseHelper.SNAKE_VALIDATOR.findall(text)) and text.islower()

    @staticmethod
    def is_upper_camel(text: str) -> bool:
        return len([char for char in text if char.isupper()]) == len(CaseHelper.UPPER_CAMEL_VALIDATOR.findall(text)) \
               and text[0].isupper()

    @staticmethod
    def to_snake(text: str):
        return '_'.join(x.lower() for x in CaseHelper.UPPER_CAMEL_VALIDATOR.findall(text))

    @staticmethod
    def to_upper_camel(text: str) -> str:
        return ''.join(x.title() for x in CaseHelper.SNAKE_VALIDATOR.findall(text))
