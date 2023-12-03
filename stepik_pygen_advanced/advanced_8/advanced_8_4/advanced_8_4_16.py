a, b, c = input().split()
print(['NO', "YES"][set(a) == set(b) == set(c)])
