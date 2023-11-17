def final_value_after_operations(operations: list[str], start: int = 0) -> int:
    for operation in operations:
        start = start - 1 if "-" in operation else start + 1
    return start
