import sys

data = [line.lstrip() for line in sys.stdin if line.lstrip().startswith('#')]
print(len(data))
