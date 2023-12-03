rows = int(input())
all_data = [list(map(int, input().split())) for elem in range(rows)]
total_1, total_2, total_3, total_4 = 0, 0, 0, 0

for l in all_data:
    if l[0] > 0 and l[1] > 0:
        total_1 += 1
    elif l[0] < 0 and l[1] > 0:
        total_2 += 1
    elif l[0] < 0 and l[1] < 0:
        total_3 += 1
    elif l[0] > 0 and l[1] < 0:
        total_4 += 1

print(f'Первая четверть: {total_1}', f'Вторая четверть: {total_2}', f'Третья четверть: {total_3}', f'Четвертая четверть: {total_4}', sep='\n')
