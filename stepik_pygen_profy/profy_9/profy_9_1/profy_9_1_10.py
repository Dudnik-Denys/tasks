def is_greater(lists: list[list[int]], number: int) -> bool:
    return len([sum(seq) for seq in lists if sum(seq) > number]) >= 1
