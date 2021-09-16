# *** Система управлениями базами данных (СУБД) SQLite3 ***

import sqlite3 as sql

# Создание базы данных с таблицей test
# with sql.connect("test.db") as db: 
#     # объект курсора
#     cursor = db.cursor()
#     # Передача команд на языке SQL
#     cursor.execute(
#         """CREATE TABLE IF NOT EXISTS test
#          (login TEXT, id INTEGER)"""
#     )
#     # закрепление изменений
#     db.commit()

# запись в БД
# with sql.connect("test.db") as db: 
#     # объект курсора ("Панель управления")
#     cursor = db.cursor()
#     # передача команд на языке SQL
#     cursor.execute(
#        "INSERT INTO test VALUES (?, ?)",
#        ("Hello", 777) 
#     )
#     # закрепление изменений
#     db.commit()

# чтение из БД
with sql.connect("test.db") as db: 
    # объект курсора ("Панель управления")
    cursor = db.cursor()
    # передача команд на языке SQL
    cursor.execute(
        "SELECT * FROM test"
    )
    # # чтение записи по одной
    # result = cursor.fetchone()
    # print(result)
    # # чтение записи по одной
    # result = cursor.fetchone()
    # print(result)
    # # чтение записи по одной
    # result = cursor.fetchone()
    # print(result)

    # чтение всех записей из таблицы
    result = cursor. fetchall()
    print(result)
   