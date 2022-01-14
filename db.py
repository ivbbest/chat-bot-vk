import sqlite3 as sq


try:
    connect = sq.connect('product.db')

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
         'https://vk.com/public210116210?z=photo-210116210_457239020%2Fwall-210116210_2'),
        (1, 'Хлеб', 'Хлеб овсяный', 'Хлеб овсяный - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239018%2Fwall-210116210_2'),
        (1, 'Хлеб', 'Хлеб белый', 'Хлеб белый - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239019%2Fwall-210116210_2'),
        (2, 'Торт', 'Торт Киевский', 'Торт Киевский - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239021%2Fwall-210116210_3'),
        (2, 'Торт', 'Торт Наполеон', 'Торт Наполеон - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239022%2Fwall-210116210_3'),
        (2, 'Торт', 'Торт Медовик', 'Торт Медовик - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239023%2Fwall-210116210_3'),
        (3, 'Пирожки', 'Пирожок с капустой', 'Пирожок с капустой - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239024%2Fwall-210116210_4'),
        (3, 'Пирожки', 'Пирожок мясной', 'Пирожок мясной - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239025%2Fwall-210116210_4'),
        (3, 'Пирожки', 'Пирожок фруктовый', 'Пирожок фруктовый - очень вкусный из натуральных продуктов',
         'https://vk.com/public210116210?z=photo-210116210_457239026%2Fwall-210116210_4'),
    ]

    with connect:
        connect.executemany(sql, data)

    # проверка на все ли ок при записи в базу данных
    # with connect:
    #     data = connect.execute("SELECT * FROM PRODUCT")
    #     for row in data:
    #         print(row)
except sq.Error as error:
    print("Ошибка при подключении к sqlite", error)
