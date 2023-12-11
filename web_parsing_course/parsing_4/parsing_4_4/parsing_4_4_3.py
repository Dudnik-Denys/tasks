import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile


response = requests.get('https://parsinger.ru/downloads/cooking_soup/index.zip', stream=True)

with open('index.zip', 'wb') as download_zip:
    for chunk in response.iter_content(chunk_size=100_000):
        download_zip.write(chunk)

with ZipFile('index.zip') as zip_file:
    zip_file.extractall()

with open('index.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)
