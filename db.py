import sqlite3 as sq

db_file = 'product.db'


def create_db(db):
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

        sql = 'INSERT INTO PRODUCT (id_category, category, product, description, url) values(?, ?, ?, ?, ?)'

        data = [
            (1, 'Хлеб', 'Хлеб ржаной', 'Хлеб ржаной - очень вкусный из натуральных продуктов',
             '-210116210_457239020'),
            (1, 'Хлеб', 'Хлеб овсяный', 'Хлеб овсяный - очень вкусный из натуральных продуктов',
             '-210116210_457239018'),
            (1, 'Хлеб', 'Хлеб белый', 'Хлеб белый - очень вкусный из натуральных продуктов',
             '-210116210_457239019'),
            (2, 'Торт', 'Торт Киевский', 'Торт Киевский - очень вкусный из натуральных продуктов',
             '-210116210_457239021'),
            (2, 'Торт', 'Торт Наполеон', 'Торт Наполеон - очень вкусный из натуральных продуктов',
             '-210116210_457239022'),
            (2, 'Торт', 'Торт Медовик', 'Торт Медовик - очень вкусный из натуральных продуктов',
             '-210116210_457239023'),
            (3, 'Пирожки', 'Пирожок с капустой', 'Пирожок с капустой - очень вкусный из натуральных продуктов',
             '-210116210_457239024'),
            (3, 'Пирожки', 'Пирожок мясной', 'Пирожок мясной - очень вкусный из натуральных продуктов',
             '-210116210_457239025'),
            (3, 'Пирожки', 'Пирожок фруктовый', 'Пирожок фруктовый - очень вкусный из натуральных продуктов',
             '-210116210_457239026'),
        ]
        with connect:
            connect.executemany(sql, data)

    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)


def select_db(db):
    try:
        connect = sq.connect(db)

        with connect:
            data = connect.execute("SELECT * FROM PRODUCT WHERE category='Хлеб'")
            for row in data:
                print(row)
    except sq.Error as error:
        print("Ошибка при подключении к sqlite", error)


# create_db(db_file)
select_db(db_file)
