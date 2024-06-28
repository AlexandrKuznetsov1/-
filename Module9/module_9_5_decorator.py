# -*- coding: utf-8 -*-

# Домашнее задание по теме "Декораторы"
# Задание: Декораторы в Python
#
# Цель задания:
# Освоить механизмы создания декораторов Python.
# Практически применить знания, создав функцию декоратор и обернув ею другую функцию.
#
# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three).
# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.

from sympy import isprime
import time

print('слегка усложним задачу и решим 2-мя способами:')

def time_track(func):
    def surrogate(*args):
        started_at = time.perf_counter_ns ()
        result = func(*args)
        ended_at = time.perf_counter_ns ()
        elapsed = ended_at - started_at
        print(f'Время работы функции {elapsed} наносекунд')
        return result
    return surrogate


@time_track
def is_prime(func):

    def simplicity_number(*args):
        itog = func(*args)
        simplicity = isprime(itog)
        if simplicity:
            return f'{itog} - Простое число'
        return f'{itog} - Составное число'
    return simplicity_number


@is_prime
def sum_three(*args):
    d = sum(args)
    return d


result1 = sum_three(1, 2, 3)
print(result1)

result2 = sum_three(1, 5, 1)
print(result2)


@time_track
def is_prime1(func):
    def wrapper(*args):
        result = func(*args)
        if result <= 1:
            return f'{result} - Составное число'
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                return f'{result} - Составное число'
        return f'{result} - Простое число'
    return wrapper


@is_prime1
def sum_three1(*args):
    return sum(args)


result3 = sum_three1(2, 3, 6)
print(result3)

result4 = sum_three1(3, 3, 6)
print(result4)

print('Иногда использование встроенных функций влечет увеличение времени отработки кода')
