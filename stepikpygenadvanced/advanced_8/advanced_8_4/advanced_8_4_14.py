str_1, str_2 = input(), input()
print(['NO', 'YES'][len(set(str_1 + str_2)) == 10])
