def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i: matrix[i - 1] for i in range(1, len(matrix) + 1)}
