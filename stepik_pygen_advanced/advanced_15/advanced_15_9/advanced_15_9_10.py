abscissas = map(float, input().split())
ordinates = map(float, input().split())
applicates = map(float, input().split())
print(all(map(lambda x: (x[0] ** 2 + x[1] ** 2 + x[2] ** 2) <= 2 ** 2, zip(abscissas, ordinates, applicates))))
