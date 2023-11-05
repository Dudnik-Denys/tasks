import sys

data = [line.strip() for line in sys.stdin]

not_int = 0
int_sum = 0

for line in data:
    try:
        if len(line.replace('.', '')) < len(line):
            int_sum += float(line)
        else:
            int_sum += int(line)
    except ValueError:
        not_int += 1

print(int_sum, not_int, sep='\n')
