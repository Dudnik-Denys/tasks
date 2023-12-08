import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    img = soup.find('img')

    print(img)


response = requests.get('https://parsinger.ru/4.1/1/index.html')
response.encoding = 'utf-8'
get_html(response.text)
