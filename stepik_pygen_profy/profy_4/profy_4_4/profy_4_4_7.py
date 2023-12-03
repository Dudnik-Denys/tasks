import json

with open('data.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

new_data = []

for item in data:
    if isinstance(item, str):
        new_data.append(item + '!')
    elif type(item) in (int, float):
        new_data.append(item + 1)
    elif type(item) == bool:
        new_data.append(not item)
    elif isinstance(item, list):
        new_data.append(item * 2)
    elif isinstance(item, dict):
        item.update({"newkey": None})
        new_data.append(item)

print(data)
print(new_data)

with open('updated_data.json', 'w', encoding='utf-8') as updated_json:
    json.dump(new_data, updated_json, indent=3)
