

# Домашнее задание по теме "Генераторы"
# Цель работы
# Более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.
# Задание
# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.
# Примечание
# Используйте оператор yield

#
# Часто задаваемые вопросы:
# один из вариантов функции генерирующей все последовательные подстроки
# def all_variants(text):
# for start in range(len(text)):
# for end in range(start+1, len(text)+1):
# yield text[start:end]

def all_variants(text):
    my_text = []
    for letter in text:
        my_text.append(letter)
        yield letter
    sum_letters = [x + y for x in text for y in my_text if x != y and x != text[-1]]
    """ Далее можно было бы пойти следующим путем: 
    print(sum_letters)  # проверяем результат полученных последовательностей
    yield sum_letters[0]  # и возвращаем нам необходимые по индексам
    yield sum_letters[-1]
    yield text 
    но так как нам нужна функция на лету необходим еще один цикл:"""

    for i in sum_letters:
        if i == my_text[0] + my_text[1] or i == my_text[1] + my_text[-1]:
            yield i
    yield text


""" Данный генератор по условию предназначен для любых строк из 3 символов, 
с другим количеством символов поведение изменится"""

a = all_variants("abc")
for i in a:
    print(i)
b = all_variants("Вот")
for i in b:
    print(i)

print('В процессе выполнения задания было найдено интересное решение подобной задачи \n'
      'с использованием цикла и библиотеки itertools:')

import itertools
def all_variants(my_str):
     #принимаем список
    temp_list = []  # создаем пустой список
    for lst_1 in range(1, len(my_str) + 1):
        # Используя цикл и библиотеку itertools создаем матрицу кортежей
        #всех последовательностей входящей строки
        temp_list.append(list(itertools.combinations(my_str, lst_1)))
    for lst_2 in temp_list:  # проходимся по временному списку
        for lst_3 in lst_2:  # проходимся по вложенному списку
            if ''.join(lst_3) != 'ac':
                yield ''.join(lst_3)


a = all_variants("abc")
for i in a:
    print(i)

print('Но данный код ломается при других символах строки:')
b = all_variants("Нет")
for i in b:
    print(i)
