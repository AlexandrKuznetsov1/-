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

person = []


class MyException(Exception):

    def __init__(self, name, age, index):
        self.__name = name
        self.age = age
        self.index = index


def get_person(name, age, index):
    person.append(name)
    minage = 16
    maxage = 70
    if minage < age < maxage:
        person.append(age)
        if '@' in index:
            if '.ru' or '.com' in index:
                person.append(index)  # устанавливаем Е.mail, если он допустимый
                return print(f'Клиент успешно зарегистрирован {person}')
            raise MyException('InvalidIndexError2', 'Введен некорректный "E-mail"', f'{index}')
        else: # иначе генерируем исключение
            raise MyException('InvalidIndexError2', 'Введен некорректный "E-mail"', f'{index}')
    else:  # иначе генерируем исключение
        raise MyException('InvalidAgeError2', 'Возрастное ограничение', 'от 16 до 70 лет')


def set_person():
    name = input('Введите имя: ')
    if not name:
        raise MyException('InvalidNameError', 'Имя не должно быть пустым', f'{name}')
    age = int(input('Возраст: '))
    if not age:
        raise MyException('InvalidAgeError', 'Введены неверные данные возраст', f'{age}')
    index = input('E-mail: ')
    if not index:
        raise MyException('InvalidIndexError', 'Поле "E-mail" не должно быть пустым', f'{index}')
    else:
        return get_person(name, age, index)


try:
    you = set_person()
except MyException as exc:
    print(exc)
