filename = input()

with open(filename, 'r', encoding='utf-8') as file:
    [print(line.strip()) for line in file.readlines()[-10:]]
