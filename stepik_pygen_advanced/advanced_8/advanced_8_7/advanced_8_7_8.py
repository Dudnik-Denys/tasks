set_1, set_2 = set(input()), set(input())
print(['YES', 'NO'][len(set_1 & set_2) == 0])
