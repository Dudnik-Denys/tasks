set_1, set_2, set_3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
set_1_2 = set_1 & set_2
print(*sorted(set_1_2.difference(set_3), reverse=True))
