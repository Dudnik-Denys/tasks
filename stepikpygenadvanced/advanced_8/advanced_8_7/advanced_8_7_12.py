set_1, set_2, set_3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
set_4 = set_1 | set_2
print(*sorted(set_3 - set_4, reverse=True))
