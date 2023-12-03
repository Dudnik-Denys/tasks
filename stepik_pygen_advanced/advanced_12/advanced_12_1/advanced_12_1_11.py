import random

n = int(input())    # количество попыток

for i in range(n):
    coin = random.randint(0, 1)
    if coin == 0:
        print('Орел')
    else:
        print('Решка')
