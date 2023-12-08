import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find(attrs={'class': 'description_detail class1 class2 class3',
                           'data-fdg45': 'value13',
                           'data-54dfg60': 'value14',
                           'data-d6f50hg': 'value15'})

    print(tag.text)


response = requests.get('https://parsinger.ru/4.1/1/index2.html')
response.encoding = 'utf-8'
get_html(response.text)
