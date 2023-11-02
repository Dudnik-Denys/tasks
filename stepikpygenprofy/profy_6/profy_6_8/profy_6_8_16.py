import sys

data = sorted({line.strip().split()[0]: int(line.strip().split()[1]) for line in sys.stdin}.items(), key=lambda x: x[1])
print(data)
