import requests

response = requests.get('https://parsinger.ru/video_downloads/videoplayback.mp4', stream=True)

with open('file.mp4', 'wb') as file:
    for chunk in response.iter_content(chunk_size=100_000):
        file.write(chunk)
