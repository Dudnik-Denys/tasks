def print_digits(number: int):
    if len(str(number)) > 1:
        print_digits(int(str(number)[1:]))
        print(str(number)[0])
    else:
        print(number)


# Alternative

# def print_digits(number):
#     if number < 10:
#         print(number)
#     else:
#         print(number % 10)
#         print_digits(number // 10)
