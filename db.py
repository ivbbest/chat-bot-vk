import sqlite3 as sq
from config import menu, db
import sys


def create_db():
    """
    Cоздание базы данных с информацией
    """
    try:
        connect = sq.connect(db)

        with connect:
            connect.execute("""
                CREATE TABLE IF NOT EXISTS PRODUCT (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_category INTEGER,
                    category TEXT,
                    product TEXT,
                    description TEXT,
                    url TEXT
                );
            """)

        sql = 'INSERT INTO PRODUCT (category, product, description, url) values(?, ?, ?, ?)'

        with connect:
            connect.executemany(sql, menu)
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    except Exception as e:
        print('Error user name', e, type(e), sys.exc_info()[-1].tb_lineno)


def select_all_category():
    """
    Выбрать только уникальные категории из базы
    """
    try:
        connect = sq.connect(db)
        category = list()

        with connect:
            data = connect.execute("""SELECT DISTINCT category FROM PRODUCT""")

            for row in data:
                category.append(row)

            return [cat[0] for cat in category]
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    except Exception as e:
        print('Error user name', e, type(e), sys.exc_info()[-1].tb_lineno)


def select_all_menu(category):
    """
    Выбрать название товара, описание и картинку, которая уже на стене висит
    """
    try:
        connect = sq.connect(db)
        info_menu = list()

        with connect:
            sql_query = """SELECT product, description, url FROM PRODUCT WHERE category=?"""
            data = connect.execute(sql_query, (category.capitalize(),))

            for row in data:
                info_menu.append(row)

            return [product for product in info_menu]
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    except Exception as e:
        print('Error user name', e, type(e), sys.exc_info()[-1].tb_lineno)


def select_all_product():
    """
    Выбрать все продукты из базы
    """
    try:
        connect = sq.connect(db)
        product = list()

        with connect:
            data = connect.execute("""SELECT DISTINCT product FROM PRODUCT""")
            for row in data:
                product.append(row)

            return [prod[0] for prod in product]
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)
    except Exception as e:
        print('Error user name', e, type(e), sys.exc_info()[-1].tb_lineno)
