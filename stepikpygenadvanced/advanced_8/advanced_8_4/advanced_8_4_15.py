str_1, str_2 = input(), input()
print(['NO', 'YES'][sorted(set(str_1)) == sorted(set(str_2))])
