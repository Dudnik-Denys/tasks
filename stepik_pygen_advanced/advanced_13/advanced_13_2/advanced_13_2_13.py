from fractions import Fraction

n = int(input())
arr = set()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % j != 0 and (i % 2 != 0 or j % 2 != 0) and i < j:
            arr.add(Fraction(f'{i}/{j}'))

for x in sorted(arr):
    print(x)
