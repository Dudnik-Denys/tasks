import random
from string import ascii_uppercase
from string import ascii_lowercase
from string import digits

digits = digits[2:]
ascii_uppercase = ascii_uppercase.replace('O', '').replace('I', '')
ascii_lowercase = ascii_lowercase.replace('o', '').replace('l', '')
total = ascii_lowercase + ascii_uppercase + digits


def generate_password(length):
    nums = 0
    big = 0
    small = 0
    password = ''

    while nums == 0 and small == 0 and big == 0:
        password = ''.join(random.sample(total, length))
        for char in password:
            if char.isupper():
                big += 1
            elif char.islower():
                small += 1
            elif char.isdigit():
                nums += 1

        if big > 0 and small > 0 and nums > 0:
            return password
        else:
            nums, small, big = 0, 0, 0


def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n, m = int(input()), int(input())

[print(code) for code in generate_passwords(n, m)]
