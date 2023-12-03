with open('population.txt', mode='r', encoding='utf-8') as file:
    text = [line.strip().split('\t') for line in file.readlines()]
    text = {line[0]: int(line[1]) for line in text if line[0][0] == 'G' and int(line[1]) > 500_000}

print(*text, sep='\n')
