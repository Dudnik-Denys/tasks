# nums = list(range(1, (int(input())) + 1))
# d = {num: [] for num in nums}
#
# for key in d.keys():
#     for num in nums:
#         if sum([int(x) for x in str(num)]) == key:
#             d[key].append(num)
#             nums.remove(num)
#     if nums:
#         for num in nums:
#             if sum([int(x) for x in str(num)]) == key:
#                 d[key].append(num)
#                 nums.remove(num)
#
# print(len(max([value for value in d.values() if value], key=len)))


# Гениальное решение автора курса
# data = {}
#
# for i in range(1, int(input()) + 1):
#     sum_of_digits = sum(map(lambda d: int(d), str(i)))
#     data[sum_of_digits] = data.get(sum_of_digits, 0) + 1
#
# print(max(data.values()))
