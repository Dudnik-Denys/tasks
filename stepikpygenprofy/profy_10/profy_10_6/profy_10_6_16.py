def is_prime(number):
    return all(number % i != 0 for i in range(2, number)) if number > 2 else False
