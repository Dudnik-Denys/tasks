import csv
import json

with open('playgrounds.csv', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';', )
    parser = {}

    for line in reader:
        if line['AdmArea'] not in parser:
            parser[line['AdmArea']] = {line['District']: [line['Address']]}
        else:
            if line['District'] not in parser[line['AdmArea']]:
                parser[line['AdmArea']].update({line['District']: [line['Address']]})
            else:
                parser[line['AdmArea']][line['District']].append(line['Address'])

with open('addresses.json', 'w', encoding='utf-8') as json_file:
    json.dump(parser, json_file, indent=3, ensure_ascii=False)
