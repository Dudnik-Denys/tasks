import requests

response = requests.get('https://parsinger.ru/4.6/1/res.json').json()
result = {}

for item in response:
    total = int(item['article']) * item['description']['rating']
    result[item['categories']] = result.get(item['categories'], 0) + total

print(result)
