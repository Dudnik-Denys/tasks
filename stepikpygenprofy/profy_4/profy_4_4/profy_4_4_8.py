import json

with open('data1.json', encoding='utf-8') as data1, open('data2.json', encoding='utf-8') as data2, open('data_merge.json', 'w', encoding='utf-8') as data_merge:
    json_data1 = json.load(data1)
    json_data2 = json.load(data2)
    json.dump(json_data1 | json_data2, data_merge, indent=3)
