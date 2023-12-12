import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.8/7/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
total = sum(int(num.text) for num in soup.select('div.tables-container td') if int(num.text) % 3 == 0)
print(total)
