from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_data = OrderedDict()

for i in range(len(data)):
    if i % 2 == 0:
        item = data.popitem(last=False)
        new_data[item[0]] = item[1]
    else:
        item = data.popitem()
        new_data[item[0]] = item[1]

print(new_data)
