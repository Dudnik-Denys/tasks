def is_integer(string: str) -> bool:
    try:
        int(string)
    except ValueError:
        return False
    return True
