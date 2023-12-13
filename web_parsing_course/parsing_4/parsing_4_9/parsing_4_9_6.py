import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://parsinger.ru/html/'


def get_response(link: str) -> str:
    response = requests.get(link)
    response.encoding = 'utf-8'
    return response.text


soup = BeautifulSoup(get_response('https://parsinger.ru/html/index1_page_1.html'), 'lxml')
categories = [link['href'] for link in soup.select('div.nav_menu a')]
result = []

for category in categories:
    soup = BeautifulSoup(get_response(URL + category), 'lxml')
    pages = [link['href'] for link in soup.select_one('div.pagen').select('a')]
    for page in pages:
        soup = BeautifulSoup(get_response(URL + page), 'lxml')
        items = soup.select('div.item')
        for item in items:
            columns = iter(['column1', 'column2', 'column3', 'column4'])
            temp = {'Название': item.select_one('a.name_item').text.strip()}
            description = dict(li.text.split(':') for li in item.select_one('div.description').select('li'))
            description = {next(columns): value.strip() for key, value in description.items()}
            temp |= description
            temp |= {'Цена': item.select_one('p.price').text}
            result.append(temp)

with open('result.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=list(result[0].keys()), delimiter=';')
    writer.writeheader()
    writer.writerows(result)
