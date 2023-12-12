import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/4/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
green_nums_sum = sum(float(num.text) for num in soup.select('td.green'))
print(green_nums_sum)
