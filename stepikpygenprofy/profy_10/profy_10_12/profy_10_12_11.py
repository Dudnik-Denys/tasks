from itertools import permutations

data = input()

for tpl in sorted(set(permutations(data))):
    print(''.join(tpl))
