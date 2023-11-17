def just_number(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def primes(left, right):
    for x in range(left, right + 1):
        if just_number(x):
            yield x
