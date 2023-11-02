import random

length = int(input())    # длина пароля

for _ in range(length):
    char = random.randint(65, 122)
    while 90 < char < 97:
        char = random.randint(65, 122)

    print(chr(char), end='')
