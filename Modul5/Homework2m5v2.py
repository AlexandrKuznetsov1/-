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
        print('Вы находитесь на', self.numberOfFloors, 'этаже') # Для проверки
    def setNewNumberOfFloors(self, floors):  # Создан метод setNewNumberOfFloors(floors)
        self.numberOfFloors = floors # который изменяет атрибут numberOfFloors на параметр floors
        print('Вы приехали на', self.numberOfFloors, 'этаж')  # и выводит в консоль numberOfFloors

my_house = House()
floors = int(input('Ведите нужный этаж : ', ))
my_house.setNewNumberOfFloors(floors)
