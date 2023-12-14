import requests
from bs4 import BeautifulSoup
import json
from sys import getsizeof

URL = 'https://parsinger.ru/html/'
session = requests.Session()


def cook(link: str) -> BeautifulSoup:
    response = session.get(link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


def get_item_data(product: BeautifulSoup, url: str) -> dict:
    data = {'categories': 'mobile',
            'name': product.select_one('#p_header').text.strip(),
            'article': product.select_one('p.article').text.split(':')[1].strip(),
            'description': {li['id']: li.text.split(':')[1].strip() for li in
                           (product.select_one(f'li:nth-child({i})') for i in range(1, 11))},
            'count': product.select_one('#in_stock').text.split(':')[1].strip(),
            'price': product.select_one('#price').text,
            'old_price': product.select_one('#old_price').text,
            'link': url}
    return data


soup = cook('https://parsinger.ru/html/index2_page_1.html')
pages = (link['href'] for link in soup.select_one('div.pagen').select('a'))
result = ()

for page in pages:
    soup = cook(URL + page)
    items = (link['href'] for link in soup.select('a.name_item'))
    for item in items:
        link = URL + item
        soup = cook(link)
        item_data = get_item_data(soup, link)
        result += (item_data, )

with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
