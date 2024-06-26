# -*- coding: utf-8 -*-

# Домашнее задание по теме "Итераторы"
# Цель работы:
# Применить dunder методы iter, next в своём классе
# Задание:
# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.
# При создании и инициализации объекта этого класса создаются атрибуты:
# start – начальное значение (если значение не передано, то 0)
# end – конечное значение (если значение не передано, то 1)
# Примечание
# Значение атрибута start всегда меньше значения атрибута end
# В решении задачи не использовать list, tuple и др. встроенные типы данных.

# from itertools import filterfalse не подходит под данное задание


class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end
        if start >= end:
            raise 'Введены некорректные значения: start должен быть меньше end'

    def __iter__(self):
        return self  # в качестве точки отсчета будет использоваться self.start

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        else:
            if self.start % 2 == 0:
                self.start += 2
                return self.start - 2
            self.start += 1
            return None


en = EvenNumbers(10, 25)
for i in en:
    print(i)


