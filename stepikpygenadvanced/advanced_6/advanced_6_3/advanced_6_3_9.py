size = int(input())
pupiels = tuple(tuple(input().split()) for _ in range(size))
[print(*pupil) for pupil in pupiels]
print()
[print(*pupil) for pupil in pupiels if int(pupil[1]) > 3]
