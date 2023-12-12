import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
rows = [row.select('td') for row in soup.select('tr')[1:]]
columns = list(zip(*rows))
result = {}

for i in range(1, len(columns) + 1):
    temp = round(sum(float(elem.text) for elem in columns[i - 1]), 3)
    result[f'{i} column'] = temp

print(result)
