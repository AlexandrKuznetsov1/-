# -*- coding: utf-8 -*-

# Цель: освоить основные команды языка SQL и использовать их в коде используя SQLite3.
#
# Задача "Первые пользователи":
# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)
# Заполните её 10 записями:
# User1, example1@gmail.com, 10, 1000
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 1000
# ...
# User10, example10@gmail.com, 100, 1000
# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
# User1, example1@gmail.com, 10, 500
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# ...
# User10, example10@gmail.com, 100, 1000
# Удалите каждую 3ую запись в таблице начиная с 1ой:
# User2, example2@gmail.com, 20, 1000
# User3, example3@gmail.com, 30, 500
# User5, example5@gmail.com, 50, 500
# ...
# User9, example9@gmail.com, 90, 500
#
# Сделайте выборку всех записей при помощи fetchall(),
# где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>

import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

# Заполняем её 10 записями, после чего "хешируем" для избежания создания дубликатов
# for i in range(1, 11):
#     cursor.execute(" INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', str(i * 10), str(1000)))

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500:
# cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 !=0", (500,))

# Удаляем каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1, 11, 3):
#     cursor.execute("DELETE FROM Users WHERE id = ? ", (i,))

# Делаем выборку всех записей при помощи fetchall(), где возраст не равен 60 и выводим их в консоль
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
results = cursor.fetchall()
for result in results:
    print(f"Имя: {result[0]} | Почта: {result[1]} | Возраст: {result[2]} | Баланс: {result[3]}")


connection.commit()  # сохраняем состояние БД
connection.close()  # закрываем подключение к БД