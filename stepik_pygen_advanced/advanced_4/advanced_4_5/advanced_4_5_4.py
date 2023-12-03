n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
errors = 0

for i in range(n - 1):
    for j in range(i, n):
        if matrix[i][j] != matrix[j][i]:
            errors += 1
            break


print(['YES', 'NO'][errors > 0])
