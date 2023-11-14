def transpose(matrix: list[list]) -> list:
    matrix_iter = zip(*matrix)
    return [list(lst) for lst in matrix_iter]
