import random

with open('first_names.txt', mode='r', encoding='utf-8') as file:
    first = [line.strip() for line in file.readlines()]

with open('last_names.txt', mode='r', encoding='utf-8') as file:
    last = [line.strip() for line in file.readlines()]

for _ in range(3):
    print(random.choice(first), random.choice(last))
