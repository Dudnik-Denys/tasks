files = [input() for _ in range(int(input()))]

for filename in files:
    with open(filename, 'r', encoding='utf-8') as file, open('output.txt', 'a', encoding='utf-8') as output:
        inp = [line for line in file.readlines()]
        output.writelines(inp)

# 2
# input1.txt
# input2.txt
