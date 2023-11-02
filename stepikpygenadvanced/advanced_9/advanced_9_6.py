first = set(map(int, input().split()))
second = set(map(int, input().split()))
lst = sorted(first & second, reverse=True)

if len(lst) > 0:
    print(*lst)
else:
    print('BAD DAY')
