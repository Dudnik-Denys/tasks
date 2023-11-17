def simple_sequence():
    number = 1
    while True:
        for _ in range(number):
            yield number
        number += 1
