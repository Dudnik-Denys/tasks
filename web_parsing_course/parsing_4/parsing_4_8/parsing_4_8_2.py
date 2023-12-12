import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/1/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
rows = soup.select('tr')[1:]
nums = set()

for row in rows:
    temp = set(float(num.text) for num in row.select('td'))
    nums |= temp

print(sum(nums))
