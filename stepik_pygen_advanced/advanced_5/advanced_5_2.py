n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
[print(*line) for line in matrix]
new = []


for i in range(n):
    for j in range(n):
        if j >= n - i - 1:
            new.append(matrix[i][j])

print(max(new))
