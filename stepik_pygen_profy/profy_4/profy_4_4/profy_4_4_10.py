import json

with open('countries.json', encoding='utf-8') as countries:
    data = json.load(countries)

religions = {}

for line in data:
    if line['religion'] not in religions:
        religions[line['religion']] = [line['country']]
    else:
        religions[line['religion']].append(line['country'])

with open('religion.json', 'w', encoding='utf-8') as religions_json:
    json.dump(religions, religions_json, indent=3)
