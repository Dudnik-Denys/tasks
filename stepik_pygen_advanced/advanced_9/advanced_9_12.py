m = int(input())
n = int(input())
pupiels = set()

for block in range(1):
    for pupil in range(n):
        pupiels.add(input())

lst = []

if m > 1:
    for block in range(m - 1):
        new = set()
        for pupil in range(int(input())):
            new.add(input())
        k = pupiels & new
        for i in k:
            lst.append(i)

    finish = [name for name in sorted(lst) if lst.count(name) == m - 1]
    finish = sorted(set(finish))

    for x in finish:
        print(x)

else:
    for y in sorted(pupiels):
        print(y)

# n = int(input())
# result = {input() for _ in range(int(input()))}
#
# for _ in range(n - 1):
#     result &= {input() for _ in range(int(input()))}
#
# print(*sorted(result), sep='\n')
