import requests
import sys
import time


class VKLongPoll:
    def __init__(self, token, group_id, version):
        self.key = None
        self.server = None
        self.ts = 0
        self.wait = 20
        self.session = requests.Session()
        self.v = version
        self.token = token
        self.id = group_id
        self.url = 'https://api.vk.com/method/'

        self.connect()

    def connect(self):
        """
        Возвращает данные для подключения к Bots Longpoll API.
        """
        response = self.method('groups.getLongPollServer', {'group_id': self.id})

        try:
            self.server = response['response']['server']
            self.key = response['response']['key']
            self.ts = response['response']['ts']
            return '[LongPoll] Connection TRUE!'
        except Exception as e:
            print('response = ', response)
            print('Error user name', e, type(e), sys.exc_info()[-1].tb_lineno)

    def check(self):
        """
        Проверка корректности информации
        """
        values = {
            'act': 'a_check',
            'key': self.key,
            'ts': self.ts,
            'wait': self.wait
        }

        response = self.session.get(
            self.server,
            params=values,
            timeout=25
        ).json()

        if 'failed' not in response:
            self.ts = response['ts']
            return response['updates']
        elif response['failed'] > 0:
            self.connect()

    def listen(self):
        """
        Прослушиваем входящую информацию в чат боте
        """
        while True:
            try:
                for event in self.check():
                    yield event
            except (requests.exceptions.ConnectionError, TimeoutError,
                    requests.exceptions.Timeout,
                    requests.exceptions.ConnectTimeout,
                    requests.exceptions.ReadTimeout):
                print("\n Переподключение к серверам ВК \n")
                time.sleep(3)

    def method(self, method, values):
        """
        Абстрактный метод, чтобы отправлять разные запросы из VK API
        """
        values = values.copy() if values else {}
        values['access_token'] = self.token
        values['v'] = self.v

        response = self.session.post(self.url + method, values).json()

        if 'error' in response:
            print('ERROR:\n' + response['error']['error_msg'])
            return False
        else:
            return response

    def send_message(self, user_id, text, keyboard=None, template=None, random_id=0):
        """
        В зависимости от параметров:
        1. Отправка в чат-боте клавиатуры и кнопок.
        2. Отправка в чат-боте карусели из сообщений из картинки,
        шаблона, title, description
        """
        values = {
            'user_id': user_id,
            'message': text,
            'keyboard': keyboard,
            'template': template,
            'random_id': random_id
        }

        self.method('messages.send', values)

    def users_name_get(self, user_id=None):
        """
        Получить имя пользователя
        """
        try:
            users_url = self.url + 'users.get'
            user_params = {
                'count': 1000,
                'user_id': user_id,
            }
            res = requests.get(users_url, params={
                'access_token': self.token,
                'v': self.v,
                **user_params
            }
                               )

            return res.json()['response'][0]['first_name']
        except Exception as e:
            print('Error user name', e, type(e), sys.exc_info()[-1].tb_lineno)
