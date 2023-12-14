import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import json

# Базовый урл к которому мы будем добавлять ссылки на категорию/страницу/товар
URL = 'https://parsinger.ru/html/'

session = requests.Session()  # Создаем сессию


# Готовим супчик :)
def cook(link: str) -> BeautifulSoup:
    response = session.get(link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# Парсинг информации о товаре
def get_item_data(product: BeautifulSoup, url: str, product_type: str) -> dict:
    data = {'categories': product_type,
            'name': product.select_one('#p_header').text.strip(),
            'article': product.select_one('p.article').text.split(':')[1].strip(),
            'description': {li['id']: li.text.split(':')[1].strip() for li in
                            (product.select_one(f'li:nth-child({i})') for i in
                            range(1, len(product.select_one('#description').select('li')) + 1))},
            'count': product.select_one('#in_stock').text.split(':')[1].strip(),
            'price': product.select_one('#price').text,
            'old_price': product.select_one('#old_price').text,
            'link': url}
    return data


Category = namedtuple('Category', ['link', 'name'])  # Создаем шаблон категории

# Получаем категории с именами и ссылками
soup = cook('https://parsinger.ru/html/index1_page_1.html')
categories = (Category(tag['href'], tag.select_one('div')['id']) for tag in soup.select_one('div.nav_menu').select('a'))

result = ()  # Итоговый кортеж с информацией о товарах

# Перебор всех товаров
for category in categories:
    soup = cook(URL + category.link)
    pages = (link['href'] for link in soup.select_one('div.pagen').select('a'))
    for page in pages:
        soup = cook(URL + page)
        items = (link['href'] for link in soup.select('a.name_item'))
        for item in items:
            link = URL + item
            soup = cook(link)
            item_data = get_item_data(soup, link, category.name)
            result += (item_data, )

# Запись результата в JSON-файл
with open('result.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
