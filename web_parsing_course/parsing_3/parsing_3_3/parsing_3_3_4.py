import requests

url = 'https://parsinger.ru/3.3/2/'
total = 0

for i in range(1, 201):
    response = requests.get(url + f'{i}.html')
    total += response.status_code

print(total)
