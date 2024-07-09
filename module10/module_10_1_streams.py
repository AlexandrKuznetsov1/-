# -*- coding: utf-8 -*-
import time
# Домашнее задание по теме "Создание потоков".
# Цель задания:
#
# Освоить механизмы создания потоков в Python.
# Практически применить знания, создав и запустив несколько потоков.
#
# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.
#
# Примечание:
# Используйте методы: start() для старта потока, join() для заморозки дальнейшей интерпретации,
# пока процессы не завершаться.
# Для установки интервала в 1 секунду используйте функцию sleep() из модуля time,
# предварительно импортировав его.

from threading import Thread


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


def func(*args, **kwargs):
    for i in args:
        print(i)
        time.sleep(1)


def func1(*args, **kwargs):
    for i in args:
        print(i)
        time.sleep(1.001)


Thread(target=func, args=list_numbers).start()
Thread(target=func1, args=list_letters).start()

# """с использованием .join()"""
#
# a = Thread(target=func, args=list_numbers)
# b = Thread(target=func1, args=list_letters)
#
# a.start()
# b.start()
# a.join()
# b.join()