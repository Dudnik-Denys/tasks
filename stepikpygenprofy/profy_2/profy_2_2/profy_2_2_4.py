sequence = input().split()
print(*sorted({int(num) for num in sequence if sequence.count(num) > 1}))
