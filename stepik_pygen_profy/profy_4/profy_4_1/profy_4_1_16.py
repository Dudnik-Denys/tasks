import sys

news = [[part.strip() for part in line.split('/')] for line in sys.stdin]
topic = ''.join(news[-1])
news = news[:-1]

categories = {}

for line in news:
    category = line[1]
    data = (float(line[2]), line[0])
    if category not in categories:
        categories[category] = [data]
    else:
        categories[category].append(data)

[print(line[1]) for line in sorted(categories[topic], key=lambda x: (x[0], x[1]))]
