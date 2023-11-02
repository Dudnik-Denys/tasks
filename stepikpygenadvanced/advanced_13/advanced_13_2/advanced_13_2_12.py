n = int(input())

if n % 2 == 0:
    one = int((n / 2) - 1)
else:
    one = int(n / 2)

two = n - one

for i in range(int(n / 2)):
    if one % two != 0 and one % 2 != 0 or two % 2 != 0:
        print(f'{one}/{two}')
        break
    else:
        one -= 1
        two += 1
