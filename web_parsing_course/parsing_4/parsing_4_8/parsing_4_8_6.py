import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.select('tr')[1:]
total = 0

for row in rows:
    orange = float(row.select_one('td.orange').text)
    blue = float(row.select('td')[-1].text)
    total = total + (orange * blue)

print(total)
