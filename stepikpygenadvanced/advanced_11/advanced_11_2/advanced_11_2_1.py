dnk = {'C': 'G',
       'G': 'C',
       'T': 'A',
       'A': 'U'}

for char in input():
    if char in dnk:
        print(dnk[char], end='')
