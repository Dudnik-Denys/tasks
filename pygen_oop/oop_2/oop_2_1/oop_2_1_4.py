def make_dartboard(n):
    matrix = [[1] * n for _ in range(n)]
    step = 1
    while step < n - step:
        for row in range(step, n - step):
            for column in range(step, n - step):
                matrix[row][column] += 1
                [print(*line) for line in matrix]
        step += 1
    return matrix


size = int(input())
dartboard = make_dartboard(size)

[print(*line) for line in dartboard]
