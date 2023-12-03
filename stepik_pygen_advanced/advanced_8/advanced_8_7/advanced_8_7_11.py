set_1, set_2, set_3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
print(*sorted((set_1 | set_2 | set_3) - (set_1 & set_2 & set_3)))
