import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('a', {'class': 'name_item product_name'}, href=True)
    for tag in tags:
        print(tag.text.strip())


response = requests.get('https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
get_html(response.text)
