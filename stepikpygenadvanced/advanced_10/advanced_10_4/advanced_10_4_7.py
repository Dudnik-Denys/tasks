secret = input()
dct = {}

for _ in range(int(input())):
    data = input()
    dct[data[0]] = int(data[-1])

for char in secret:
    cnt = secret.count(char)
    for key, value in dct.items():
        if value == cnt:
            secret = secret.replace(char, key)

print(secret)
