n = int(input())
cmn = []
final = []
data = [set(input()) for elem in range(n)]

for line in data:
    for num in line:
        cmn.append(num)

for num in cmn:
    if cmn.count(num) == n:
        final.append(num)

print(*sorted(set(final)))


# n = int(input())
# numbers = [input() for _ in range(n)]
#
# num_set = set(numbers[0]).intersection(*numbers)
# print(*sorted(num_set))
