import requests

url = 'https://parsinger.ru/img_download/img/ready/'

for i in range(1, 161):
    with open(f'img{i}.png', 'wb') as img:
        response = requests.get(url + f'{i}.png')
        img.write(response.content)
