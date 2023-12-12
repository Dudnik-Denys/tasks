import requests
from bs4 import BeautifulSoup
import json

response = requests.get('https://parsinger.ru/4.8/6/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
headers = [header.text for header in soup.select_one('thead tr').select('th')]
cars = soup.select('tbody tr')
result = []

for car in cars:
    car = [param.text for param in car]
    temp = dict(zip(headers, car))
    temp['Год выпуска'], temp['Стоимость авто'] = int(temp['Год выпуска']), int(temp['Стоимость авто'])
    if temp['Год выпуска'] >= 2005 and temp['Стоимость авто'] <= 4_000_000 and temp['Тип двигателя'] == 'Бензиновый':
        result.append({'Марка Авто': temp['Марка Авто'], 'Год выпуска': temp['Год выпуска'],
                       'Тип двигателя': temp['Тип двигателя'], 'Стоимость авто': temp['Стоимость авто']})

result = sorted(result, key=lambda x: x['Стоимость авто'])
print(json.dumps(result, indent=4, ensure_ascii=False))
