from itertools import product

number_system = '0123456789ABCDEF'


def sequence(system: int, length: int):
    result = sorted(''.join(tpl) for tpl in product(number_system[:system], repeat=length))
    return result


n, m = int(input()), int(input())

print(*sequence(n, m))
