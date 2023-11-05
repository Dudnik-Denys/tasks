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
        raise ValueError
    if len(string) < 9:
        raise LengthError
    if sum([symbol.isupper() for symbol in string]) == 0:
        raise LetterError
    if sum([symbol.islower() for symbol in string]) == 0:
        raise LetterError
    if sum([symbol.isdigit() for symbol in string]) == 0:
        raise DigitError
    return True


try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))
