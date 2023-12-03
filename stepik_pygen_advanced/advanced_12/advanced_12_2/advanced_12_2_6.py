import random


def generate_ip() -> str:
    ip = []

    for _ in range(4):
        num = random.randint(0, 255)
        ip.append(str(num))

    ip = '.'.join(ip)

    return ip


# from random import *
#
#
# def generate_ip():
#     return '.'.join([str(randint(0, 255)) for _ in range(4)])
