import json


def total_items_count(companies: dict) -> int:
    total = 0
    for value in companies.values():
        total += value
    return total


with open('food_services.json', encoding='utf-8') as json_file:
    data = json.load(json_file)
    parser = {}
    counts_of_restaurants = {}

    for line in data:
        if line['District'] not in parser:
            parser[line['District']] = {line['OperatingCompany']: 1}
        elif line['District'] in parser and line['OperatingCompany'] not in parser[line['District']]:
            parser[line['District']].update({line['OperatingCompany']: 1})
        elif line['District'] in parser and line['OperatingCompany'] in parser[line['District']]:
            parser[line['District']][line['OperatingCompany']] += 1

    for district in parser.values():
        for company, count in district.items():
            if company not in counts_of_restaurants:
                counts_of_restaurants[company] = count
            else:
                counts_of_restaurants[company] += count

    districts = sorted(parser.items(), key=lambda item: total_items_count(item[1]), reverse=True)
    counts_of_restaurants = sorted(counts_of_restaurants.items(), key=lambda x: x[1], reverse=True)
    biggest_operating_company = counts_of_restaurants[1]
    most_restaurants_district = districts[0]

    print(f'{most_restaurants_district[0]}: {total_items_count(most_restaurants_district[1])}\n'
          f'{biggest_operating_company[0]}: {biggest_operating_company[1]}')
