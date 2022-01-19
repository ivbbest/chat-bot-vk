import unittest
from vk.vk import VKLongPoll
from config import token, group_id, version


user = VKLongPoll(token, group_id, version)
msg = '[LongPoll] Connection TRUE!'
id1 = 1
id2 = 115056659


class TestStringMethods(unittest.TestCase):
    def test_users_name_get(self):
        self.assertEqual(user.users_name_get(id1), 'Павел')
        self.assertEqual(user.users_name_get(id2), 'Владимир')

    def test_connect(self):
        self.assertEqual(user.connect(), msg)


if __name__ == '__main__':
    unittest.main()
