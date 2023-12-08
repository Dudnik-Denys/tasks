import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    emails = soup.select('.email_field strong')
    emails = [tag.next_sibling.strip() for tag in emails]

    return emails


response = requests.get('https://parsinger.ru/4.1/1/index5.html')
response.encoding = 'utf-8'
print(get_html(response.text))
