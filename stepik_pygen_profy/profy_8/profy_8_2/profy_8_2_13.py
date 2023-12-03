def print_digits(number: int):
    if number < 10:
        print(number)
    else:
        print_digits(number // 10)
        print(number % 10)
