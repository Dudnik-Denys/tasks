telephones = [input().lower().split() for _ in range(int(input()))]
numbers = {}

for user in telephones:
    if user[1] not in numbers:
        numbers[user[1]] = [user[0]]
    elif user[1] in numbers:
        numbers[user[1]].append(user[0])

for _ in range(int(input())):
    user = input().lower()
    if user in numbers:
        print(*numbers[user])
    elif user not in numbers:
        print('абонент не найден')

# dct = {}
# for _ in range(int(input())):
#     phone, name = input().lower().split()
#     dct.setdefault(name, []).append(phone)
# for _ in range(int(input())):
#     print(*dct.get(input().lower(), ['абонент не найден']))
