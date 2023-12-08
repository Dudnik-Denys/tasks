import requests
from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    prices = soup.select('p.product_price')

    count = 0
    for price in prices:
        num = ''.join([digit for digit in price.text if digit.isdigit()])
        count += int(num)

    return count


response = requests.get('https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
print(get_html(response.text))
