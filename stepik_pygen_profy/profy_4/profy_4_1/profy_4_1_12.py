import sys

data = [line.strip() for line in sys.stdin]

if int(data[-1]) % 2 == 0 and len(data) % 2 == 0:
    print('Дима')
elif int(data[-1]) % 2 != 0 and len(data) % 2 == 0:
    print('Анри')
elif int(data[-1]) % 2 == 0 and len(data) % 2 != 0:
    print('Анри')
elif int(data[-1]) % 2 != 0 and len(data) % 2 != 0:
    print('Дима')
