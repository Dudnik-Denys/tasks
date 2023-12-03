import random

lotery = []

for _ in range(7):
    num = random.randint(1, 49)
    while num in lotery:
        num = random.randint(1, 49)

    lotery.append(num)

print(*sorted(lotery))


# import random
#
# s = set()
#
# while len(s) < 7:
#     s.add(random.randint(1, 49))
#
# print(*sorted(s))
