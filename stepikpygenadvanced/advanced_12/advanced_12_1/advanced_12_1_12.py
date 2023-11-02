import random

n = int(input())    # количество попыток

for _ in range(n):
    print(random.randint(1, 6))
