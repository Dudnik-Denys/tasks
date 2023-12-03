s = input()


def count(string: str) -> int:
    total = 0
    max_total = 0

    if 'Р' in string:
        total = 1
        max_total = 1
        for i in range(len(string) - 1):
            if string[i] == 'Р' and string[i + 1] == 'Р':
                total += 1
                if total > max_total:
                    max_total = total
            else:
                total = 1

    return max_total


print(count(s))

# s = input()
# seq = s.split("О")  # убираем всех орлов и группируем решек
#
# mx = 0  # максимум подряд идущих решек
# for el in seq:
#     mx = max(mx, el.count("Р"))
#
# print(mx)
