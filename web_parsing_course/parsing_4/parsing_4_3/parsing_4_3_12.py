import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags_li = soup.select('body li')
    for tag in tags_li:
        print(tag['id'])


response = requests.get('https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
get_html(response.text)
