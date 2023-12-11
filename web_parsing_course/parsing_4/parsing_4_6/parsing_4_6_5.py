from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/'
response = requests.get('https://parsinger.ru/html/index3_page_4.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
pages = (link['href'] for link in soup.select_one('div.pagen').select('a'))
articles_sum = 0

for page in pages:
    response = requests.get(url + page)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    articles_links = [link['href'] for link in soup.select('div.sale_button a')]
    for link in articles_links:
        response = requests.get(url + link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        articles_sum += int(soup.select_one('p.article').text.split(' ')[1])

print(articles_sum)
