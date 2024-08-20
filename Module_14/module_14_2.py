# -*- coding: utf-8 -*-

# Цель: научится использовать функции внутри запросов языка SQL и использовать их в решении задачи.
#
# Задача "Средний баланс пользователя":
# Для решения этой задачи вам понадобится решение предыдущей.
# Для решения необходимо дополнить существующий код:
# Удалите из базы данных not_telegram.db запись с id = 6.
# Подсчитать общее количество записей.
# Посчитать сумму всех балансов.
# Вывести в консоль средний баланс всех пользователя.

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
# cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
# results = cursor.fetchall()
# for result in results:
#     print(f"Имя: {result[0]} | Почта: {result[1]} | Возраст: {result[2]} | Баланс: {result[3]}")

# Удаляем из базы данных not_telegram.db запись с id = 6:
# cursor.execute("DELETE FROM Users WHERE id = ? ", (6,))

# Подсчитать общее количество записей, посчитать сумму всех балансов:
# cursor.execute("SELECT (*) FROM Users")
# extreme_results = cursor.fetchall()
# total_users = 0
# all_balances = 0
# for i in extreme_results:
#     total_users += 1
#     all_balances += i[4]

# другой вариант:
cursor.execute("SELECT COUNT (id) FROM Users")
# extreme_results = cursor.fetchall()
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM (balance) FROM Users")
all_balances = cursor.fetchone()[0]

# Вывести в консоль средний баланс всех пользователя.
print(all_balances/total_users)

connection.commit()  # сохраняем состояние БД
connection.close()  # закрываем подключение к БД