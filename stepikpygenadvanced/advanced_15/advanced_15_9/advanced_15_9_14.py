pupils = [[input() for _ in range(int(input()))] for _ in range(int(input()))]
cnt = 0

for lst in pupils:
    if any(map(lambda x: '5' in x, lst)):
       cnt += 1

print(['NO', 'YES'][cnt == len(pupils)])
