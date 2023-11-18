def num_jewels_in_stones(jewels: str, stones: str) -> int:
    count = 0
    for gem in jewels:
        count += stones.count(gem)

    return count
