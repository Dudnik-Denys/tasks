from collections import Counter
import json

with open('zoo.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    counter = Counter()

    for animals in data:
        counter.update(animals)

print(counter.total())
