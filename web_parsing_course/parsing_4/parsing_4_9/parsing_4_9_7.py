import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://parsinger.ru/html/'  # Базовый урл к которому мы будем добавлять ссылки на категорию/страницу/товар


# Приготовление супа
def cook(link: str) -> BeautifulSoup:
    response = requests.get(link)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')


# Парсинг информации о товаре
def get_item_data(product: BeautifulSoup) -> dict:
    data = {'Наименование': product.select_one('#p_header').text.strip(),
            'Артикул': product.select_one('p.article').text.split(':')[1].strip()}
    description = dict([li.text.split(':') for li in [product.select_one(f'li:nth-child({i})') for i in range(1, 3)]])
    description = {key.strip(): value.strip() for key, value in description.items()}
    description.update({'Наличие': product.select_one('#in_stock').text.split(':')[1].strip(),
                        'Цена': product.select_one('#price').text,
                        'Старая цена': product.select_one('#old_price').text})
    data |= description
    return data


# Получение категорий
soup = cook('https://parsinger.ru/html/index1_page_1.html')
categories = [link['href'] for link in soup.select_one('div.nav_menu').select('a')]

# Итоговый список товаров
result = []

# Перебор всех товаров
for category in categories:
    soup = cook(URL + category)
    pages = [link['href'] for link in soup.select_one('div.pagen').select('a')]
    for page in pages:
        soup = cook(URL + page)
        items = [link['href'] for link in soup.select('a.name_item')]
        for item in items:
            soup = cook(URL + item)
            item_data = get_item_data(soup)
            item_data |= {'Ссылка': URL + item}
            result.append(item_data)

# запись в файл
with open('result.csv', 'w', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=list(result[0].keys()), delimiter=';')
    writer.writeheader()
    writer.writerows(result)
