from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/'
response = requests.get('https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
categories = [link['href'] for link in soup.select_one('div.nav_menu').select('a')]
total = 0

for category in categories:
    response = requests.get(url + category)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    pages = (link['href'] for link in soup.select_one('div.pagen').select('a'))
    for page in pages:
        response = requests.get(url + page)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        articles = [link['href'] for link in soup.select('a.name_item')]
        for article in articles:
            response = requests.get(url + article)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')
            price = int(soup.select_one('#price').text.split(' ')[0])
            stock = int(soup.select_one('#in_stock').text.split(':')[1])
            total += (price * stock)

print(total)
