first = set(map(int, input().split()))
second = set(map(int, input().split()))

if first == second and len(first) == len(second):
    print('YES')
else:
    print('NO')
