str_1, str_2 = set(map(int, input().split())), set(map(int, input().split()))
print(*sorted(str_1 - str_2))
