import random

matrix = random.sample(range(1, 76), 25)
matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
matrix[2][2] = 0
[print(*row) for row in matrix]
