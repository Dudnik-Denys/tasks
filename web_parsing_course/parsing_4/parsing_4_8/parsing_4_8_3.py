import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/2/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.select('tr')[1:]
total = sum(float(row.select_one('td').text) for row in rows)
print(total)
