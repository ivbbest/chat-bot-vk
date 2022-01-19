from config import version, group_id, token
from vk.vk import VKLongPoll
from vk.keyboard import VkKeyboard
from vk.template_carousel import create_template_carousel
from random import randint
import db
import time
import sys


def main():
    vk = VKLongPoll(token, group_id, version)
    keywords = [key.lower() for key in db.select_all_category()]

    try:
        for event in vk.listen():
            if event['type'] == 'message_new':
                user_id = int(event['object']['message']['from_id'])
                body = event['object']['message']['text']
                name_user = vk.users_name_get(user_id)

                choice_keyboard = VkKeyboard()
                choice_keyboard.create_keyboard(menu=False)
                vk.send_message(user_id, f'{name_user}, привет. Тебе показать наше меню?',
                                keyboard=choice_keyboard.get_keyboard(),
                                random_id=randint(0, 100))

                if body.lower() == 'да':
                    time.sleep(2)
                    menu_keyboard = VkKeyboard()
                    menu_keyboard.create_keyboard()
                    vk.send_message(user_id, 'Вот наша продукция. Выбирай;-)',
                                    keyboard=menu_keyboard.get_keyboard(),
                                    random_id=randint(0, 100))

                elif body.lower() == 'назад':
                    vk.send_message(user_id, '')
                    continue

                elif body.lower() in keywords:
                    vk.send_message(user_id, f'{name_user}, ты выбрал категорию {body}',
                                             template=create_template_carousel(body),
                                             random_id=randint(0, 100))
                    time.sleep(1)

                    vk.send_message(user_id, 'Еще вот что у нас в меню',
                                    keyboard=menu_keyboard.get_keyboard(),
                                    random_id=randint(0, 100))

                elif body.lower() == 'нет':
                    vk.send_message(user_id, f'Если не хотите, то тогда, чем я могу помочь, {name_user} ',
                                    random_id=randint(0, 100))
                    continue
                elif body.lower() == 'завершить':
                    vk.send_message(user_id, f'{name_user}, c тобой было очень приятно. Пока;-)',
                                    random_id=randint(0, 100))
                    break

            else:
                print(event)
    except Exception as e:
        print('Error user name', e, type(e), sys.exc_info()[-1].tb_lineno)


if __name__ == '__main__':
    main()
