from config import version, group_id, token
from vk import VKLongPoll
from keyboard import VkKeyboard
from template_carousel import create_template_carousel
from random import randint
import db


def create_keyword():
    """
    Получение всех категорий и использования для анализа в чат-боте, что выбирает пользователь
    """
    keyword = db.select_all_category()

    return [key.lower() for key in keyword]


def main():
    vk = VKLongPoll(token, group_id, version)
    keywords = create_keyword()

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
                menu_keyboard = VkKeyboard()
                menu_keyboard.create_keyboard()
                vk.send_message(user_id, 'Вот наша продукция. Выбирай;-)',
                                keyboard=menu_keyboard.get_keyboard(),
                                random_id=randint(0, 100))

            elif body.lower() == 'назад':
                vk.send_message(user_id, '')
                continue

            elif body.lower() in keywords:
                vk.send_message_carousel(user_id, f'Выбрал категорию {body.capitalize()}',
                                         template=create_template_carousel(body),
                                         random_id=randint(0, 100))
                vk.send_message(user_id, 'Еще вот что у нас в меню',
                                keyboard=menu_keyboard.get_keyboard(),
                                random_id=randint(0, 100))

            elif body.lower() == 'нет':
                vk.send_message(user_id, 'На нет и суда нет;-)',
                                random_id=randint(0, 100))
                continue
            elif body.lower() == 'завершить':
                vk.send_message(user_id, f'{name_user}, c тобой было очень приятно. Пока;-)',
                                random_id=randint(0, 100))
                break

        else:
            print(event)


if __name__ == '__main__':
    main()
