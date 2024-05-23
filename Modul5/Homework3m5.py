# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности self.numberOfFloors
# и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию

class Buiding:
    def __init__(self, *argse):  # Создаем инициализатор для класса Buiding
        self.numberOfFloors = []  # задаем целочисленный атрибут этажности
        self.buildingType = []  # и строковый атрибут
        for i in argse:
            if isinstance(i, int):
                self.numberOfFloors.append(i)
            if isinstance(i, str):
                self.buildingType.append(i)
    def __eq__(self, other):
        #print(self, other)  #для проверки объектов
        #print(self.numberOfFloors, other.numberOfFloors)  #для проверки значений объектов
        #print(self.buildingType, other.buildingType)  #для проверки значений объектов
        if self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType:
            return print('Мы соседи')
        print('Будем знакомы... ')
my_buiding = Buiding(1, 'этаж')
you_buiding = Buiding(1, 'этаж')

if Buiding.__eq__(self=my_buiding,other=you_buiding):
    print()