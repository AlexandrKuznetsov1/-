# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности self.numberOfFloors
# и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию

class Buiding:
    def __init__(self, Floor, Type):  # Создаем инициализатор для класса Buiding
        self.numberOfFloors = int(Floor)  # задаем целочисленный атрибут этажности
        self.buildingType = str(Type)  # и строковый атрибут
    def __eq__(self, other):  # Создаем __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

House1 = Buiding(9, "Кирпичный")
House2 = Buiding(12, 'Панельный')
House3 = Buiding(9, "Кирпичный")

print(House1 == House2)
print(House1 == House3)
print(House2 == House3)