from functools import total_ordering


@total_ordering
class RomanNumeral:
    _NUMBERS = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
                'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    _FOR_REPLACE = {'IV': 'IIII', 'IX': 'VIIII', 'XL': 'XXXX', 'XC': 'LXXXX', 'CD': 'CCCC', 'CM': 'DCCCC'}

    _ROMANS = {value: key for key, value in _NUMBERS.items()}

    def __init__(self, number: str):
        self.number = number

    @staticmethod
    def to_roman(num: int) -> str:
        roman = ''
        while num > 0:
            for n, r in RomanNumeral._ROMANS.items():
                if num - n >= 0:
                    roman += r
                    num -= n
                    break
        return roman

    def __str__(self):
        return self.number

    def __int__(self):
        roman = self.number

        for num, repl in RomanNumeral._FOR_REPLACE.items():
            roman = roman.replace(num, repl) if num in roman else roman

        real_num = sum(self._NUMBERS[num] for num in roman)
        return real_num

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            result = int(self) + int(other)
            roman = RomanNumeral.to_roman(result)
            return RomanNumeral(roman) if result > 0 else NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            result = int(self) - int(other)
            roman = RomanNumeral.to_roman(result)
            return RomanNumeral(roman) if result > 0 else NotImplemented

    def __eq__(self, other):
        return int(self) == int(other) if isinstance(other, RomanNumeral) else NotImplemented

    def __gt__(self, other):
        return int(self) > int(other) if isinstance(other, RomanNumeral) else NotImplemented
