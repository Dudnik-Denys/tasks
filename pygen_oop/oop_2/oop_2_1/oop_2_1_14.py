from fractions import Fraction


def is_fraction(string: str) -> bool:
    try:
        Fraction(string)
    except Exception:
        return False
    return '/' in string
