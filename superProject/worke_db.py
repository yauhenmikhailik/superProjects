import sqlite3


try:
    connect = sqlite3.connect('db.sqlite3')

    cursor = connect.cursor()

    cursor.execute('SELECT name FROM apple_product WHERE name LIKE "A%"')
    # cursor.execute('INSERT INTO apple_category ("name") VALUES ("Новая категория")')
    a = cursor.fetchall()
    cursor.close()
    connect.commit()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    print('я выполняюсь всегда вне зависимости от ошибок')