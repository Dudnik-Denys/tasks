total = 0

with open('data.txt', encoding='utf-8') as file:
    for _ in file.readlines():
        total = total + 1

print(total)
