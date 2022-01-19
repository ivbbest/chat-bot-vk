from vk.keyboard import VkKeyboard
import json


KEYBOARD_TEST = {
    'one_time': True,
    'inline': False,
    'buttons': [
        [
            {
                'color': 'positive',
                'action': {
                    'type': 'text',
                    'payload': {'test': 'some_payload'},
                    'label': 'Test-1'
                }
            }
        ],
        []
    ]
}

keyboard = VkKeyboard()


def test_keyboard():

    keyboard.add_button(
        'Test-1',
        color='positive',
        payload={'test': 'some_payload'}
    )
    keyboard.add_line()
    breakpoint()
    assert keyboard.get_keyboard() == json.dumps(KEYBOARD_TEST, ensure_ascii=False).encode('utf-8')


if __name__ == '__main__':
    test_keyboard()
