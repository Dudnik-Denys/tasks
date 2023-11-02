n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    total = 0
    avg = sum(matrix[i]) / len(matrix[i])
    for j in range(n):
        if matrix[i][j] > avg:
            total += 1
    print(total)
