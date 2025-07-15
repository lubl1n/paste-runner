# скріпт для отримання user_key з Pastebin API

import requests

dev_key = '#'
username = '#'
password = '#'

data = {
    'api_dev_key': dev_key,
    'api_user_name': username,
    'api_user_password': password
}

resp = requests.post('https://pastebin.com/api/api_login.php', data=data)
print( resp.text)  # на виході отримаємо user_key

