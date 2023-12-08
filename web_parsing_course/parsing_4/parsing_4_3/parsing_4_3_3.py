import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find(attrs={'data-gpu': 'nVidia GeForce RTX 4060'})

    print(tag.text)


response = requests.get('https://parsinger.ru/4.1/1/index3.html')
response.encoding = 'utf-8'
get_html(response.text)
