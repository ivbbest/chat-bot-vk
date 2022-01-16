import json

MAX_BUTTONS_ON_LINE = 5
MAX_DEFAULT_LINES = 10
MAX_INLINE_LINES = 6


class VkKeyboard:
    """ Класс для создания клавиатуры для бота (https://vk.com/dev/bots_docs_3)
    :param one_time: Если True, клавиатура исчезнет после нажатия на кнопку
    :type one_time: bool
    """

    def __init__(self, one_time=False, inline=False):
        self.one_time = one_time
        self.inline = inline
        self.lines = [[]]
        self.button_type = 'text'

        self.keyboard = {
            'one_time': self.one_time,
            'inline': self.inline,
            'buttons': self.lines
        }

    def get_keyboard(self, *args, **kwargs):
        """ Получить json клавиатуры """
        return json.dumps(self.keyboard, *args, **kwargs)

    def add_button(self, label, color='secondary', payload=None):
        """ Добавить кнопку с текстом.
            Максимальное количество кнопок на строке - MAX_BUTTONS_ON_LINE
        :param label: Надпись на кнопке и текст, отправляющийся при её нажатии.
        :type label: str
        :param color: цвет кнопки.
        :type color: VkKeyboardColor or str
        :param payload: Параметр для callback api
        :type payload: str or list or dict
        """

        current_line = self.lines[-1]

        if len(current_line) >= MAX_BUTTONS_ON_LINE:
            raise ValueError(f'Max {MAX_BUTTONS_ON_LINE} buttons on a line')

        if payload is not None and not isinstance(payload, str):
            payload = json.dumps(payload)

        button_type = self.button_type

        current_line.append({
            'color': color,
            'action': {
                'type': button_type,
                'payload': payload,
                'label': label,
            }
        })

    def add_line(self):
        """ Создаёт новую строку, на которой можно размещать кнопки.
            Максимальное количество строк:
               Стандартное отображение - MAX_DEFAULT_LINES;
               Inline-отображение - MAX_INLINE_LINES.
        """
        if self.inline:
            if len(self.lines) >= MAX_INLINE_LINES:
                raise ValueError(f'Max {MAX_INLINE_LINES} lines for inline keyboard')
        else:
            if len(self.lines) >= MAX_DEFAULT_LINES:
                raise ValueError(f'Max {MAX_DEFAULT_LINES} lines for default keyboard')

        self.lines.append([])
