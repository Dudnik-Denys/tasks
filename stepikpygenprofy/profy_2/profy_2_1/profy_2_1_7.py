def is_valid(pin: str) -> str:
    return ' ' not in pin and pin.isdigit() and 6 >= len(pin) >= 4
