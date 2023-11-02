data = {
    1: ('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'),
    2: ('D', 'G'),
    3: ('B', 'C', 'M', 'P'),
    4: ('F', 'H', 'V', 'W', 'Y'),
    5: ('K', ),
    8: ('J', 'X'),
    10: ('Q', 'Z')
}

cnt = 0

for char in input():
    for key, value in data.items():
        if char in value:
            cnt += key
            break

print(cnt)
