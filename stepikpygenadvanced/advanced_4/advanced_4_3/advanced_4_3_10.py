n = int(input())


def pascal(num: int) -> list:
    base_list = [1]
    if num == 0:
        return [1]
    if num > 0:
        for i in range(1, n + 1):
            new_list = [1]
            for j in range(len(base_list) - 1):
                new_elem = base_list[j] + base_list[j + 1]
                new_list.append(new_elem)
            new_list.append(1)
            base_list = new_list
        return base_list


print(pascal(n))
