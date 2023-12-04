from decimal import Decimal


def is_decimal(string: str) -> bool:
    try:
        Decimal(string)
    except Exception:
        return False
    return True
