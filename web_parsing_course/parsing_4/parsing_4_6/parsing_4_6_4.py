from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/'
response = requests.get('https://parsinger.ru/html/index3_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pages = (link['href'] for link in soup.select_one('div.pagen').select('a'))
items = []

for page in pages:
    response = requests.get(url + page)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    items.extend(item.text.strip() for item in soup.select('a.name_item'))

print(items)
