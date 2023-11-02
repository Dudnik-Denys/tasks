n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
maximum = matrix[0][0]

for i in range(n):
    for j in range(n):
        if j <= i <= n-1-j or j >= i >= n-1-j:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]

print(maximum)
