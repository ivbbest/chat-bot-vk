import sys
import random
from settings import token, version, group_id
from vk import VKLongPoll


def main():
    vk = VKLongPoll(token, group_id, version)

    for event in vk.listen():
        if event['type'] == 'message_new':
            user_id = int(event['object']['message']['from_id'])
            body = event['object']['message']['text']
            print('%d: %s' % (user_id, body))

        elif event['type'] == 'message_reply':
            if 'from_id' in event['object']:
                print('REPLY from %d: %s' % (event['object']['from_id'], event['object']['text']))
            else:
                print('REPLY from BOT')

        elif event['type'] == 'group_join':
            pass
        elif event['type'] == 'group_leave':
            pass
        elif event['type'] == 'message_typing_state':
            pass

        else:
            print(event)


if __name__ == '__main__':
    main()
