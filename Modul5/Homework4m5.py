# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса
# Building total (по примеру класса Lemming из урока)
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print


class Buiding:  # Создали новый класс Buiding
    total = 0  # с атрибутом total

    def __init__(self):  # Создан инициализатор для класса Buiding
        Buiding.total +=1  # который будет увеличивать атрибут количества созданных объектов класса

house = []
while len(house) < 40:  # В цикле создаем 40 объектов класса Building
    new_house = Buiding()
    house.append(new_house)
    print(new_house)  # и выводим их на экран
print(Buiding.total)  # для проверки количества объектов
