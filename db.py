import sqlite3 as sq
from settings import menu, db


# создание базы данных с информацией
def create_db():
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


# выбрать только уникальные категории из базы
def select_all_category():
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


# выбрать название товара, описание и картинку, которая уже на стене висит
def select_all_menu(category):
    try:
        connect = sq.connect(db)
        info_menu = list()

        with connect:
            sql_query = """SELECT product, description, url FROM PRODUCT WHERE category=?"""
            data = connect.execute(sql_query, (category,))

            for row in data:
                info_menu.append(row)

            return [product for product in info_menu]
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)


# выбрать все продукты из базы
def select_all_product():
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

# create_db()
# select_all_category()
# print(select_all_menu('Хлеб'))
