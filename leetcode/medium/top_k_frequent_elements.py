def top_k_frequent(nums: list[int], k: int) -> list[int]:
    if len(nums) == len(set(nums)):
        return nums[:k]
    new = {}
    for i in range(len(nums)):
        if nums[i] in new:
            new[nums[i]] = new[nums[i]] + 1
        elif nums[i] not in new:
            new[nums[i]] = 1

    result = [i[0] for i in sorted(new.items(), key=lambda x: x[1], reverse=True)]

    return result[:k]
