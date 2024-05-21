#Домашнее задание по уроку "Пространство имен"

#Создайте новый проект в PyCharm
#Запустите созданный проект
#Ваша задача:
#Создайте новый класс House
#Задайте ему новый атрибут numberOfFloors = 10
#В цикле пройдитесь по атрибуту numberOfFloors и распечайте значение "Текущий этаж равен"
#Полученный код напишите в ответ к домашему заданию

class House: #Создан новый класс House
    def __init__(self):
        self.numberOfFloors = 10  # Задан новый атрибут numberOfFloors = 10
    def __add__(self, item):
        print("Текущий этаж равен :", item)


my_house = House()
a = 0
while a < my_house.numberOfFloors:
    a = a + 1
    my_house.__add__(a)
    continue









