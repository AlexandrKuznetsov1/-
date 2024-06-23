# -*- coding: utf-8 -*-

# Домашнее задание по теме "Создание исключений".
# Цель задания:
#
# Освоить механизмы создания и обработки исключений в Python.
# Научиться создавать собственные исключения, наследуя классы от Exception. Попрактиковаться в передаче исключений
# дальше по стеку вызовов.
#
# Задание:
#
# Создайте новый проект или продолжите работу в текущем проекте.
# Создайте минимум два своих собственных исключения, наследуя их от класса
# Exception
#
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработайте.


class MyException(Exception):
    """
    Содержит сообщения об исключении и информацию о допустимых параметров возраста
    """

    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
                f"Возраст должен быть в диапазоне от {self.minage} до {self.maxage}"


class InvalidData(MyException):
    """
    Содержит сообщения об исключении и информацию о допустимых параметров E.mail
    """

    def __init__(self, index):
        self.index = index

    def __str__(self):
        return f'E.mail {self.index} некорректный. ' \
                f'Должен содержать символы "@" и "."'

class Person:
    """
    Принимает параметры пользователя при регистрации
    """
    def __init__(self, name, age, index):
        """
        Генерирует исключения при вводе некорректных данных
        """
        self.__name = name  # устанавливаем имя
        minage, maxage = 1, 110
        self.index_trail = index
        if minage < age < maxage:  # устанавливаем возраст, если передано корректное значение
            self.__age = age
        else:  # иначе генерируем исключение
            raise MyException(age, minage, maxage)
        if '@' in self.index_trail:
            if '.' in self.index_trail:
                self.index = index  # устанавливаем Е.mail, если он допустимый
        else: # иначе генерируем исключение
            raise InvalidData(index)

    def display_info(self):
        """
        Выводит на экран данные пользователя при успешной регистрации
        """
        print(f"Имя: {self.__name}, Возраст: {self.__age}, E.mail: {self.index}")


try:
    alex = Person("Александр", 49, 'Alex@urban.ru')
    alex.display_info()  # Имя: Александр  Возраст: 49 E.mail: Alex@urban.ru

except MyException as e:
    print(e)  # Недопустимое значение

try:
    jack = Person("Женя", -23, 'Jack@motor.com')
    jack.display_info()
except MyException as e:
    print(e)  # Недопустимое значение

try:
    user = Person("Юся", 12, 'user.com')
    user.display_info()
except MyException as e:
    print(e)  # Недопустимое значение

try:
    user2 = Person("Юсик", -3, 'user.com')
    user2.display_info()
except MyException as e:
    print(e)  # Недопустимое значение