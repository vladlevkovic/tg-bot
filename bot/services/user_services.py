import json

def user_register(user_id, username):
    try:
        file_path = 'D:/GoIteens_lesson/python_1y_18_25_05/bot/bot/data/users.json'
        data = []
        with open(file_path, 'r') as f:
            data.append(json.load(f))

        data.append({'user_id': user_id, 'username': username})

        with open(file_path, 'w') as f:
            json.dump(data, f)

        return True
    except Exception as e:
        print(e)
