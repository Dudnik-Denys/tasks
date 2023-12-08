import requests

response = requests.get('https://parsinger.ru/3.4/1/json_weather.json').json()

for data in response:
    data['Температура воздуха'] = int(''.join([num for num in data['Температура воздуха'] if num.isdigit() or num == '-']))

print(sorted(response, key=lambda x: x['Температура воздуха'])[0]['Дата'])
