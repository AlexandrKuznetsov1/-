

# Задание до обновления платформы:
immutable_var_ = 'кортеж-the tuple', 2024, 35.5, 'tuple_',
print(immutable_var_)
immutable_var1_ = immutable_var_, 'списки', 2026
print(immutable_var1_)
print('Объект кортеж предназначен для хранения не изменяемых данных. При создании кортежа все внесенные в него данные получают свой индекс, для возможности быстрого обращения к ним, в том числе другие кортежи')
mutable_list = ['значения элементов в списках можно менять', 42,]
print(mutable_list)
mutable_list.append('значения элементов в кортеже изменить нельзя')
print(mutable_list)
mutable_list.extend("Urban")
print(mutable_list)
mutable_list.remove(42)
print(mutable_list)
print(mutable_list[0])

# Практическая работа по уроку "Организация программ и методы строк."
# Организуйте программу:
# Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
# Вывести длину символов введённого текста
# Работа с методами строк:
# Используя методы строк, выполните следующие действия:
# Выведите строку my_string в верхнем регистре.
# Выведите строку my_string в нижнем регистре.
# Измените строку my_string, удалив все пробелы.
# Выведите первый символ строки my_string.
# Выведите последний символ строки my_string.

print('Введите текст:')
my_string = input('=>')
print(my_string)
print(len(list(my_string)))
print(my_string.upper())
print(my_string.lower())
my_string1 = my_string.replace(' ', '')
print(my_string1)
print(my_string[0])
print(my_string[-1])

