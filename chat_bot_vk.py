import requests
import configparser
import json

# Получаем из конфига токен для вк
config = configparser.ConfigParser()
config.read("settings.ini")
token = config["VK"]["token"]
version = '5.131'
group_id = '210116210'

# получение ответа от сервера
data = requests.get('https://api.vk.com/method/groups.getLongPollServer',
                    params={'access_token': token, 'v': version, 'group_id': group_id}).json()[
    'response']
print(data)

# отправление запроса на Long Poll сервер со временем ожидания 90 секунд и опциями ответа 2
while True:
    response = requests.get(
        '{server}?act=a_check&key={key}&ts={ts}&wait=25'.format(
            server=data['server'], key=data['key'], ts=data['ts'])).json()

    print(response['updates'])
