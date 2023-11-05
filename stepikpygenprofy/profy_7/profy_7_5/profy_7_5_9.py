class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    if not isinstance(string, str):
        return ValueError
    if len(string) < 9:
        return LengthError.__name__
    if sum([symbol.isupper() for symbol in string]) == 0:
        return LetterError.__name__
    if sum([symbol.islower() for symbol in string]) == 0:
        return LetterError.__name__
    if sum([symbol.isdigit() for symbol in string]) == 0:
        return DigitError.__name__
    return True


password = input()

while is_good_password(password) is not True:
    print(is_good_password(password))
    password = input()

print('Success!')
