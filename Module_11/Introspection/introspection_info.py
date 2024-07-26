# -*- coding: utf-8 -*-

# Цель задания:
#
# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
#
# Задание:
# Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и
# проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.
#
# 1. Создайте функцию introspection_info(obj), которая принимает объект obj.
# 2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
# 3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
#    - Тип объекта.
#    - Атрибуты объекта.
#    - Методы объекта.
#    - Модуль, к которому объект принадлежит.
#    - Другие интересные свойства объекта, учитывая его тип (по желанию).

import inspect
from pprint import pprint
from colorama import Fore, init
init(autoreset=True)


def introspection_info(obj):
    CheckObject.printer_start(1)
    print(obj)
    type_obj = type(obj)
    methods_obj = []
    if inspect.getmodule(obj):
        module_obj = inspect.getmodule(obj)
    else:
        module_obj = '__main__'
    attributes_obj = []
    dict_introspection_info = {'type': type_obj, 'attributes': attributes_obj, 'methods': methods_obj, 'module': module_obj}
    for i in dir(obj):
        if "__" in i:
            methods_obj.append(i)
        else:
            if "_" not in i:
                attributes_obj.append(i)
    pprint(dict_introspection_info)
    CheckObject.printer_stop(1)


number = 49
line = 'Alex'
list1 = [number, line]
set_ = {number, line}
dict_ = {number: line}
taple1_ = (number, line, list1, set_, dict_)


class CheckObject:

    def printer_start(self):
        if self:
            print(Fore.GREEN + 'Начало работы функции "introspection_info"')

    def printer_stop(self):
        if self:
            print(Fore.CYAN + 'Конец работы функции "introspection_info"')


introspection_info(number)
introspection_info(line)
introspection_info(list1)
introspection_info(set_)
introspection_info(dict_)
introspection_info(taple1_)
introspection_info(introspection_info)
introspection_info(CheckObject)
introspection_info(Fore)
