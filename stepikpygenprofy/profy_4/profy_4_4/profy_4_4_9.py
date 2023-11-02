import json

with open('people.json', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

keys = set()

for line in json_data:
    for key in line.keys():
        keys.add(key)

for line in json_data:
    for key in keys:
        line[key] = line.get(key, None)

with open('updated_people.json', 'w', encoding='utf-8') as updated_json:
    json.dump(json_data, updated_json, indent=3)
