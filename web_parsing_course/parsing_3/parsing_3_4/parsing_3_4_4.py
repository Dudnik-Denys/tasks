import requests

response = requests.get('https://parsinger.ru/3.4/2/index.html')
response.encoding = 'utf-8'
print(response.text)
