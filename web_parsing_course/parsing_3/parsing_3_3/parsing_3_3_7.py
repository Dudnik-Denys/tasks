import requests

url = 'https://parsinger.ru/3.3/4/'

correct_links = 0
first_available_page, last_available_page = None, None

for i in range(1, 101):
    response = requests.get(url + f'{i}.html')
    correct_links += 1 if response.status_code == 200 else 0
    first_available_page = url + f'{i}.html' if correct_links == 1 else first_available_page
    last_available_page = url + f'{i}.html' if response.status_code == 200 else last_available_page

print(f"Первая доступная страница: {first_available_page}\n"
      f"Последняя доступная страница: {last_available_page}")
