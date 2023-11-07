def is_power(number: int) -> bool:
    if number == 1:
        return True
    if number != int(number):
        return False
    return is_power(number / 2)
