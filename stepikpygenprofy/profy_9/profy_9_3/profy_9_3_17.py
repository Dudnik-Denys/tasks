def print_operation_table(operation: callable, rows: int, cols: int):
    result = [[operation(m, n) for n in range(1, cols + 1)] for m in range(1, rows + 1)]
    max_elem = result[0][0]

    for row in result:
        for elem in row:
            if elem > max_elem:
                max_elem = elem

    for line in result:
        for elem in line:
            print(str(elem).ljust(len(str(max_elem)) + 1), end=' ')
        print()
