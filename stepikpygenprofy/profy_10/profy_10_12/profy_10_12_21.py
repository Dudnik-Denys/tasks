from itertools import product


def password_gen():
    yield from (''.join(str(i[0]) + str(i[1]) + str(i[2])) for i in product(range(10), repeat=3))
