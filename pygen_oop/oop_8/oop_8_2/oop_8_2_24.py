from enum import Enum


class Seasons(Enum):
    WINTER = 1
    SPRING = 2
    SUMMER = 3
    FALL = 4

    def text_value(self, code):
        translation = {'WINTER': 'зима', 'SPRING': 'весна', 'SUMMER': 'лето', 'FALL': 'осень'}
        return self.name.lower() if code == 'en' else translation[self.name]
