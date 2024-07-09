# -*- coding: utf-8 -*-

# Цель: научиться создавать классы наследованные от класса Thread.
#
# Задача "За честь и отвагу!":
# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
# осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.

# Алгоритм выполнения кода:
# # Создание класса
# first_knight = Knight('Sir Lancelot', 10)
# second_knight = Knight("Sir Galahad", 20)
# # Запуск потоков и остановка текущего
# # Вывод строки об окончании сражения

from threading import Thread
import time
from colorama import Fore, init

init(autoreset=True)
print(Fore.GREEN + "За честь и отвагу!")
time.sleep(1)


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100  # задаем количество врагов
        a = 0
        b = 0
        print(f'{self.name}, на нас напали!')
        while enemy != a:
            enemy = enemy - self.power
            b = b + 1
            time.sleep(1)
            print(f'{self.name} сражается {b} дней, осталось {enemy} врагов')
        print(f'{self.name} одержал победу спустя {b} дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
time.sleep(1.2)
print(Fore.RED + 'Битва окончена!!!')