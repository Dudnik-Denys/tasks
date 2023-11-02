nums = [int(input()) for num in range(int(input()))]
goal = int(input())


def multi(numbers: list, res: int) -> str:
    counter = 0

    for i in range(len(numbers) - 1):
        for j in numbers[i + 1:]:
            if numbers[i] * j == res:
                counter += 1
                break

    return ["НЕТ", "ДА"][counter > 0]


print(multi(nums, goal))
