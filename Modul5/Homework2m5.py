# Домашнее задание по уроку "Пространство имен"

# Создайте новый проект в PyCharm
# Запустите созданный проект
# Ваша задача:
# Создайте новый класс House
# Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
# Создайте метод setNewNumberOfFloors(floors),
# который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors

class House:  # Создан новый класс House
    def __init__(self):  # Создан инициализатор для класса House
        self.numberOfFloors = 0  # Задан атрибут этажности

my_floor = House()
attr_floor = 'floor'  # Создаем переменную attr_floor для проверки и замены атрибута
def setNewNumberOfFloors(floors):  # создаем метод, который будет изменять атрибут numberOfFloors на параметр floors
    if hasattr(my_floor, attr_floor):  # проверяем наличие атрибута в классе
        print("он есть")
    setattr(my_floor, attr_floor, floors)  # устанавливаем новое значение для атрибута numberOfFloors равное floors
    print('Вы приехали. Ваш этаж :', my_floor.floor)  # выводим полученный результат

floors = int(input('Ведите нужный этаж : ', ))
setNewNumberOfFloors(floors)  # передайте методу значения Вашего этажа
