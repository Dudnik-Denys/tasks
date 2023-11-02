import pickle


def control_sum_check(filename: str, control_sum: int) -> str:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    if isinstance(data, list):
        nums = [num for num in data if type(num) == int]
        if len(nums) > 0:
            if min(nums) * max(nums) == control_sum:
                return 'Контрольные суммы совпадают'
        return ['Контрольные суммы не совпадают', 'Контрольные суммы совпадают'][len(nums) == control_sum]

    if isinstance(data, dict):
        nums = [num for num in data.keys() if type(num) == int]
        if sum(nums) == control_sum:
            return 'Контрольные суммы совпадают'
    return 'Контрольные суммы не совпадают'


print(control_sum_check(input(), int(input())))
