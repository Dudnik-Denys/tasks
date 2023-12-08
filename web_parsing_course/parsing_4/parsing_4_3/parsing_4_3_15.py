import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    sibling = soup.select_one('section#section3 p').next_sibling

    return sibling.strip()


response = requests.get('https://parsinger.ru/4.1/1/index6.html')
response.encoding = 'utf-8'
print(get_html(response.text))
