import json

with open('food_services.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    parser = {}

    for line in data:
        if line['TypeObject'] not in parser:
            parser[line['TypeObject']] = {'Name': line['Name'], 'SeatsCount': line['SeatsCount']}
        else:
            if line['SeatsCount'] > parser[line['TypeObject']]['SeatsCount']:
                parser[line['TypeObject']] = {'Name': line['Name'], 'SeatsCount': line['SeatsCount']}

    for restaurant in sorted(parser.items()):
        type_of, params = restaurant
        print(f'{type_of}: {params["Name"]}, {params["SeatsCount"]}')
