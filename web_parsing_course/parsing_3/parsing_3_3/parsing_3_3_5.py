import requests

url = 'https://parsinger.ru/3.3/1/'

for i in range(1, 201):
    response = requests.get(url + f'{i}.html')
    print(f'response status code: {response.status_code}')
    if response.status_code == 200:
        print(response.text)
        break
