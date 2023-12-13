from bs4 import BeautifulSoup
import requests
import csv

url = 'https://parsinger.ru/html/'
response = requests.get('https://parsinger.ru/html/index1_page_1.html')
soup = BeautifulSoup(response.text, 'lxml')
pages = [link['href'] for link in soup.select_one('div.pagen').select('a')]
result = []

for page in pages:
    response = requests.get(url + page)
    soup = BeautifulSoup(response.text, 'lxml')
    items = [link['href'] for link in soup.select('a.name_item')]
    for item in items:
        temp = {}
        response = requests.get(url + item)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        info = soup.select_one('div.description')
        temp.update({'Наименование': info.select_one('#p_header').text,
                     'Артикул': info.select_one('p.article').text.split(':')[1].strip()})
        ul = {}
        for tag in info.select('#description li'):
            key, value = tag.text.split(':')
            value = value.strip()
            if key == 'Тип подключения':
                key = 'Тип'
            if key == 'Размеры':
                key = 'Размер'
            ul |= {key: value}
        temp.update(ul)
        temp.update({'Наличие': info.select_one('#in_stock').text.split(':')[1].strip(),
                     'Цена': info.select_one('#price').text, 'Старая цена': info.select_one('#old_price').text,
                     'Ссылка на карточку с товаром': response.url})
        result.append(temp)


with open('result.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=list(result[0].keys()), delimiter=';')
    writer.writeheader()
    writer.writerows(result)
