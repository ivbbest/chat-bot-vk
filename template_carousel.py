import db
import json
import sys


def create_template_carousel(category):
    """
    создание шаблона для карусели товаров
    """
    try:
        products = db.select_all_menu(category)
        product_info = list()
        for product in products:
            title, description, photo_id = product
            all_element = dict([('buttons', [{
                "action": {
                    "type": "text",
                    "label": "Заказать"
                }
            }]), ('description', description),
                                ('photo_id', photo_id), ('title', title)
                                ])
            product_info.append(all_element)

        template = dict([("type", "carousel"), ("elements", product_info)])

        return json.dumps(template)
    except Exception as e:
        print('Error template', e, type(e), sys.exc_info()[-1].tb_lineno)
