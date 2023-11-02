f = [input().split() for _ in range(int(input()))]
files = {elem[0]: elem[1:] for elem in f}
modes = {'write': 'W', 'read': 'R', 'execute': 'X'}

for i in range(int(input())):
    mode, file = input().split()
    mode = modes[mode]
    if mode in files[file]:
        print('OK')
    else:
        print('Access denied')
