def two_sum(nums: list[int], target: int) -> list[int]:
    storage = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in storage:
            return [i, storage[diff]]
        storage[n] = i
