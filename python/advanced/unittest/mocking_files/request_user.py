import requests

def request_user(user_id):
    response = requests.get(f"https://im_not_exist/{user_id}")
    if response.ok:
        return response.text
    else:
        return "Fail!"
