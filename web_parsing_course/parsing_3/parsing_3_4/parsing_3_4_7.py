import requests

url = 'https://parsinger.ru/3.4/3/dialog.json'
response = requests.get(url).json()
counter = {}


def json_analysis(user):
    counter[user['username']] = counter.get(user['username'], 0) + 1
    if len(user['comments']) >= 1:
        for commentator in user['comments']:
            json_analysis(commentator)


for user in [response]:
    json_analysis(user)

print(dict(sorted(counter.items(), key=lambda x: (-x[1], x[0]))))
