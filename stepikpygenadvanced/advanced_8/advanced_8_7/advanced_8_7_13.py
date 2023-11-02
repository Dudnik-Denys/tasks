set_1, set_2, set_3 = set(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split()))
nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(*sorted(nums - (set_1 | set_2 | set_3)))
