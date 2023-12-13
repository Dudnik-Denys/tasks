import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import json

url = 'https://parsinger.ru/html/'
response = requests.get('https://parsinger.ru/html/index4_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pages = [link['href'] for link in soup.select_one('div.pagen').select('a')]
result = []

for page in pages:
    response = requests.get(url + page)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.select('div.item')
    for item in items:
        temp = {}
        name = item.select_one('a.name_item').text.strip()
        description = dict([tag.text.split(':') for tag in item.select_one('div.description') if isinstance(tag, Tag)])
        description = {key: value.strip() for key, value in description.items()}
        price = item.select_one('p.price').text
        temp.update({'Наименование': name})
        temp.update(description)
        temp.update({'Цена': price})
        result.append(temp)

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
