with open('grades.txt') as f:
    counter = 0
    for line in f:
        if min(map(int, line.split()[1:])) >= 65:
            counter += 1
print(counter)
