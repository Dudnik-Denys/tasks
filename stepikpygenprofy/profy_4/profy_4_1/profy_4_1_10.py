import sys

data = [line.strip() for line in sys.stdin]

for line in data:
    print(line[::-1])
