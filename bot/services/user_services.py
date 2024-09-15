import json
from pathlib import Path

def user_register(user_id, username):
    try:
        file_path = './data/users.json'
        file = Path(file_path)
        if not file.exists() or file.stat().st_size == 0:
            data = []
        else:
            with open(file_path, 'r') as f:
                data = json.load(f)

        data.append({'user_id': user_id, 'username': username})

        with open(file_path, 'w') as f:
            json.dump(data, f)

        return True
    except Exception as e:
        print(e)

