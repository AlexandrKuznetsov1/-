# -*- coding: utf-8 -*-

# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - текст
# price(цена) - целое число (не пустой)
# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.

import sqlite3


connection = sqlite3.connect("database.db")

cursor = connection.cursor()


dict_foto_ = {"Drinks_Hamburger.jpg": 'Гамбургер - 970 кал.', "Butterbrot.jpg": 'Бутерброд - 1500 кал.',
              "Fast_food_Pizza.jpg": 'Пицца - 1790 кал.', "Fast_food_Hot_dog.jpg": 'Хот-дог - 2440 кал.'}


def initiate_db():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL,
        name_foto TEXT NOT NULL
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users(
        userid INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER NOT NULL,
        balance INTEGER NOT NULL
        )
        """)


initiate_db()


def get_all_products():
    cursor.execute(" SELECT * FROM Products")
    all_products = cursor.fetchall()
    return all_products


def is_included(username):
    check_user = cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
    if check_user.fetchone():
        return True
    return False


def add_user(username, email, age):
    cursor.execute(f"INSERT INTO Users(username, email, age, balance) VALUES (?, ?, ?, ?)",
                    (username, email, age, 1000))

    connection.commit()


# for i, j, k in zip(range(1, 5), dict_foto_, dict_foto_.values()):
#     initiate_db()
#     cursor.execute("INSERT INTO Products(id, title, description, price, name_foto) VALUES (?, ?, ?, ?, ?)",
#     (f'{i}', f'Product{i}', f'{k}', f'{i * 100}', f'{j}'))
#     # print(f"Название: Product{i} | Описание: {k} | Цена: {i * 100} | name_foto {j}")
#
#
# connection.commit()
# connection.close()