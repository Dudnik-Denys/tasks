import requests

response = requests.get('https://parsinger.ru/downloads/get_json/res.json').json()
result = {}

for item in response:
    total = int(item['count']) * int(item['price'].split(' ')[0])
    result[item['categories']] = result.get(item['categories'], 0) + total

print(result)
