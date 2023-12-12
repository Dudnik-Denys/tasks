import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.8/8/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
atrs = soup.find_all(attrs={'colspan': ['2', '3']})
total = 0

for atr in atrs:
    tds = atr.select('td')
    ths = atr.select('th')
    temp = tds + ths
    for element in temp:
        total += int(element.text) if element.get('colspan') is not None else 0

print(total)


# Better variant
# import requests
# from bs4 import BeautifulSoup
#
#
# response = requests.get(url='https://parsinger.ru/4.8/8/index.html')
# soup = BeautifulSoup(response.text, 'html.parser')
#
# print(sum(
#     int(item.text) for item in soup.find_all(['td', 'th'], colspan=True, string=True)
# ))
