import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/3/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
bold_numbers_sum = sum(float(num.text) for num in soup.select('td b'))

print(bold_numbers_sum)
