def index_of_nearest(numbers: list, number: int) -> int:
    nearest = {}
    if numbers:
        for num in numbers:
            nearest[num] = abs(number - num)

        minimal = min([abs(n - number) for n in numbers])
        for key, value in nearest.items():
            if value == minimal:
                return numbers.index(key)

    return -1


# def index_of_nearest(nums, n):
#     if nums:
#         minimum = min(nums, key=lambda num: abs(num - n))
#         return nums.index(minimum)
#     return -1
