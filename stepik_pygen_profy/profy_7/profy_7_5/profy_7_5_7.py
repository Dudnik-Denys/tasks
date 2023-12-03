def is_good_password(string: str) -> bool:
    if not isinstance(string, str):
        return False
    if len(string) < 9:
        return False
    if sum([symbol.isupper() for symbol in string]) == 0:
        return False
    if sum([symbol.islower() for symbol in string]) == 0:
        return False
    if sum([symbol.isdigit() for symbol in string]) == 0:
        return False
    return True
