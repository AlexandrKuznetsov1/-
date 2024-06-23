# -*- coding: utf-8 -*-
#
# Самостоятельная работа по уроку "Распаковка параметров и параметры функции"
#
# Цель задания: Освоить создание функций с параметрами по умолчанию и практику вызова этих функций
# с различным количеством аргументов.
#
# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра
# со значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
# 2.Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params,
# и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params,
# используя распаковку параметров (* для списка и ** для словаря).
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)


def print_params(a=1, b='строка', c=True):
    return print(a, b, c)

print_params()
print_params(12)
print_params('ok')
print_params(False)
print_params(12, True)
print_params('ok', 'yes', "good")
print_params(False, False, False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1975, "Alex", True]
values_dict = {'a': 1975, 'b': "Alex", 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["работает", True]
print_params(*values_list_2, 42)
