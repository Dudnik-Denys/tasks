import random


def generate_index():

    indx = []

    for _ in range(4):
        indx += chr(random.randint(65, 90))

    for i in range(2, 4):
        indx.insert(i, str(random.randint(0, 99)))

    indx.insert(3, '_')

    return ''.join(indx)


print(generate_index())
