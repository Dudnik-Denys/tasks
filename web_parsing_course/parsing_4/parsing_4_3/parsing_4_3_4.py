import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    li_tag = soup.find('li', {'data-key': 'cooling_system'}).text

    print(li_tag)


response = requests.get('https://parsinger.ru/4.1/1/index.html')
response.encoding = 'utf-8'
get_html(response.text)
