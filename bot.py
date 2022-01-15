import sys
import random
from settings import token, version, group_id
from vk import VKLongPoll


def main():
    # CONFIG = loadConfig()

    vk = VKLongPoll(token, group_id, version)

    # sql = MySQL(
    #     CONFIG['sql_host'],
    #     CONFIG['sql_user'],
    #     CONFIG['sql_pass'],
    #     CONFIG['sql_db']
    # )
    #
    # ALL_TESTS = sql.ex('SELECT * FROM rus;')
    #
    # task = Tasks(vk, sql)
    # us = User(vk, sql)

    for event in vk.listen():
        if event['type'] == 'message_new':

            user_id = int(event['object']['message']['from_id'])
            body = event['object']['message']['text']
            name_user = vk.users_name_get(user_id)
            print(name_user)

            # print('%d: %s' % (user_id, body))

            # user = us.get(user_id)
            #
            # if not user:
            #     user = us.create(user_id)
            #     vk.sendMessage(user_id,
            #                    'Привет, %s! Я тебя долго ждал.\n\nДля того что бы разобраться в моих командах, отправь мне слово *id0(помощь).' %
            #                    user[1])
            #     continue
            #
            # if body.lower() == 'рус':
            #
            #     if user[2] > 0:
            #         vk.sendMessage(user_id, 'Завершите предыдущее задание!')
            #     else:
            #         task.show(user_id, random.randint(1, ALL_TESTS), 0)
            #
            #     continue
            #
            # elif body.lower() == 'рт':
            #     if user[2] > 0:
            #         vk.sendMessage(user_id, 'Завершите предыдущее задание!')
            #     else:
            #         task_id = 81;
            #         task.show(user_id, task_id, 2)
            #
            #     continue
            #
            # elif body.lower() == 'стоп':
            #     if user[8] == 2:
            #         sql.ex(
            #             'UPDATE users SET tmp_test = 0, tmp_type = \'\', tmp_cor = 0, mode = 0, mode_true = \'\', mode_false = \'\', mode_score = 0 WHERE user_id = %d;' % user_id)
            #         vk.sendMessage(user_id, 'Вы вышли из режима РТ.')
            #
            #     continue
            #
            # elif body.lower() == 'я':
            #     us.me(user_id, user)
            #     continue
            #
            # elif body.lower() == 'топ':
            #     us.top(user_id)
            #     continue
            #
            # else:
            #     if user[2] > 0:
            #         task.convertAns(body, user_id, user)
            #     else:
            #         pass


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
