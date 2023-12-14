import requests
from bs4 import BeautifulSoup
from collections import namedtuple

URL = 'https://parsinger.ru/html/'
session = requests.Session()


def cook(link: str) -> BeautifulSoup:
    response = session.get(link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


Category = namedtuple('Category', ['link', 'name'])
soup = cook('https://parsinger.ru/html/index1_page_1.html')
categories = (Category(tag['href'], tag.select_one('div')['id']) for tag in soup.select_one('div.nav_menu').select('a'))

result = {}


for category in categories:
    soup = cook(URL + category.link)
    pages = (link['href'] for link in soup.select_one('div.pagen').select('a'))
    for page in pages:
        soup = cook(URL + page)
        items = (link['href'] for link in soup.select('a.name_item'))
        for item in items:
            soup = cook(URL + item)
            result[category.name] = result.get(category.name, 0) + int(soup.select_one('#in_stock').text.split(':')[1])

print(result)
