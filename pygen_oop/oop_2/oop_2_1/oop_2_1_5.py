sequence = input()

while '()' in sequence:
    sequence = sequence.replace('()', '')

print(len(sequence) == 0)
