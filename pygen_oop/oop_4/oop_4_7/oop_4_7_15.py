class StrExtension:
    @staticmethod
    def remove_vowels(string: str) -> str:
        vowels = 'aeiouy'
        return ''.join(char for char in string if char not in vowels and char not in vowels.upper())

    @staticmethod
    def leave_alpha(string: str) -> str:
        return ''.join(char for char in string if char.isalpha())

    @staticmethod
    def replace_all(string: str, chars: str, char: str) -> str:
        return ''.join(map(lambda x: x if x not in chars else char, string))
