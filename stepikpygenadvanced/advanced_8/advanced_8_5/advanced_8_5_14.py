data = list(map(int, input().split()))
res = []

for num in data:
    if num not in res:
        res.append(num)
        print('NO')
    else:
        print('YES')
