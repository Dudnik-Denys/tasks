mathem, inform = int(input()), int(input())
math = set(input() for _ in range(mathem))
inf = set(input() for _ in range(inform))

only_math = math - (math & inf)
print(len(only_math))
