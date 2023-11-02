import json
from zipfile import ZipFile


def is_correct_json(json_data: str):
    try:
        json.loads(json_data)
    except json.JSONDecodeError:
        return False
    return True


with ZipFile('data.zip') as archive:
    json_files = [file for file in archive.infolist() if '.json' in file.filename and not file.is_dir()]
    arsenal_players = []
    for file in json_files:
        with archive.open(file) as json_file:
            try:
                data = json_file.read().decode('utf-8')
                if is_correct_json(data):
                    player = json.loads(data)
                    if player['team'] == 'Arsenal':
                        arsenal_players.append(player['first_name'] + ' ' + player['last_name'])
            except UnicodeDecodeError:
                pass

[print(player) for player in sorted(arsenal_players)]
