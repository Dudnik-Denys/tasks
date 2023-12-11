import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/html/hdd/4/4_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

old_price = int(soup.select_one('#old_price').text.split(' ')[0])
current_price = int(soup.select_one('#price').text.split(' ')[0])
print(round((old_price - current_price) * 100 / old_price, 1))
