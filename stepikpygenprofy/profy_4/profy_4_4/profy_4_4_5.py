import json


def is_correct_json(json_data: str):
    try:
        json.loads(json_data)
    except json.JSONDecodeError:
        return False
    return True
