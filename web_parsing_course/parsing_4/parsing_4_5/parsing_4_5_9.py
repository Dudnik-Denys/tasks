import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
prices = [int(price.text.split(' ')[0]) for price in soup.select('p.price')]
print(sum(prices))
