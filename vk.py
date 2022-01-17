import requests


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
        response = self.method('groups.getLongPollServer', {'group_id': self.id})

        try:
            self.server = response['response']['server']
            self.key = response['response']['key']
            self.ts = response['response']['ts']
            print('[LongPoll] Connection TRUE!')
        except:
            print(response)

    def check(self):
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
        while True:
            for event in self.check():
                yield event

    def method(self, method, values):
        values = values.copy() if values else {}
        values['access_token'] = self.token
        values['v'] = self.v

        response = self.session.post(self.url + method, values).json()

        if 'error' in response:
            print('ERROR:\n' + response['error']['error_msg'])
            return False
        else:
            return response

    def send_message(self, user_id, text, keyboard='', random_id=0):
        values = {
            'user_id': user_id,
            'message': text,
            'keyboard': keyboard,
            'random_id': random_id,

        }

        self.method('messages.send', values)

    def send_message_carousel(self, user_id, text, random_id=0, template=''):
        values = {
            'user_id': user_id,
            'message': text,
            'random_id': random_id,
            'template': template

        }

        self.method('messages.send', values)

    # Получим имя пользователя
    def users_name_get(self, user_id=''):
        try:
            users_url = self.url + 'users.get'
            user_params = {
                'count': 1000,
                'user_id': user_id,
            }
            res = requests.get(users_url, params={'access_token': self.token, 'v': self.v, **user_params})
            return res.json()['response'][0]['first_name']
        except Exception as e:
            print('Error user name', type(e))

