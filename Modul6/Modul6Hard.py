"""
# Общее ТЗ:
# Реализовать классы Figure(родительский), Circle, Triangle и Cube,
объекты которых будут обладать методами изменения размеров, цвета и т.д.
# Многие атрибуты и методы должны быть инкапсулированы и для них должны быть написаны интерфейсы взаимодействия (методы)
 - геттеры и сеттеры.
"""

import math
from colorama import Fore


class Figure:
    """
    # содержит атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
    # Атрибуты(публичные): filled(закрашенный, bool)
    """
    sides_count = 1  # количество сторон

    def __init__(self):
        self.__sides = []
        self.__color = []
        self.filled = bool
        # print(self.__color)

    def get_color(self):
        """
        Возвращает список RGB цветов.
        """
        return self.__color

    def __is_valid_color(self, r, g, b):
        """
            Служебный метод, принимает параметры r, g, b, который проверяет корректность переданных значений перед
        установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (вкл.).
        """

        acceptable_values = list(range(0, 256))  # Создаем список корректных значений для параметров цвета
        self.valid_color = [r, g, b]
        # print(self.valid_color)
        self.filled = (all(i in acceptable_values for i in (r, g, b)))

    def set_color(self, r, g, b):
        """
            Принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
        предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
        """
        Figure.__is_valid_color(self, r, g, b)
        # print(self.filled)
        # print(r)

        if self.filled:
            self.__color = self.valid_color
        self.__color = repr(self.get_color())
        # print(self.__color)

    def set_sides(self, *args):
        """
            Принимает неограниченное кол-во сторон, проверяет корректность переданных данных, если данные корректны,
        то меняет __sides на новый список, если нет, то оставляет прежние.
        """
        list_args = [args]
        # print(args)

        for i in list_args:
            if isinstance(i, int):
                if i > 0:
                    self.__sides = list_args
                    # print(self.__sides)

            # print('Получены некорректные данные')
    def __is_valid_sides(self, sides_count=None, *args):
        """
            Служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные
        числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
        """
        list2_args = [args]
        if isinstance(args, int):
            if args > 0:                
                if len(list(list2_args)) == sides_count:
                    return True
                return False
            return False
        return False

    def __len__(self):
        """
        Возвращает периметр фигуры.
        """
        self.perimeter_figure = sum(self.__sides)
        return self.perimeter_figure


class Circle(Figure):
    """
        Обладает следующими атрибутами и методами:
        Все атрибуты и методы класса Figure
        Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
        Метод get_square,- возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
    """
    sides_count = 1

    def __init__(self, colors, *args):
        super().__init__()
        self.r = colors[0]
        self.g = colors[1]
        self.b = colors[2]
        self.__color = list(colors)
        if len(args) > self.sides_count:
            self.len_sides = 1
        self.len_sides = args[0]
        self.__radius = int(self.len_sides/2*math.pi)
        # print(self.__radius)
        # print(self.__color)
        # print(self.__dict__)

    def get_square(self):
        """
            Возвращает площадь круга
        """
        S = math.pi * (self.__radius ** 2)
        return S

    def set_sides(self, len_side):
        if len_side > 0:
            self.len_sides = [len_side]

    def get_sides(self):
        return self.len_sides

    def __len__(self):
        return self.len_sides[0]


class Triangle(Figure):
    """
        Обладает следующими атрибутами и методами:
        Все атрибуты и методы класса Figure
        Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
        Метод get_square возвращает площадь треугольника.
    """
    sides_count = 3

    def __init__(self, colors, *args):
        """
        Немного усложним и сделаем наш треугольник разносторонним и будем считать верным как одно
        передаваемое значение (для равнобедренного), так и три
        """
        super().__init__()
        self.r = colors[0]
        self.g = colors[1]
        self.b = colors[2]
        self.__sides = list(args)
        if len(args) == self.sides_count:
            self.a = self.__sides[0]
            self.b = self.__sides[1]
            self.c = self.__sides[2]
        if len(args) == 1:
            self.a = self.b = self.c = args[0]
        if len(args) != self.sides_count and len(args) != 1:
            self.a = self.b = self.c = 1
        if (self.a + self.b) < self.c:
            print('Такого треугольника не существует')
        # print(self.a)
        # print(self.b)
        # print(self.c)
        p = (self.a + self.b + self.c) / 2  # Полупериметр треугольника
        self.__height_a = (2 * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))) / self.a  #Высота с основанием а
        self.__height_b = 2 / self.b * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  #Высота с основанием в
        self.__height_c = 2 / self.c * math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))  #Высота с основанием с

    def get_sides(self):
        return [self.a, self.b, self.c]
    def get_square(self):
        S_triangle = 1 / 2 * self.a * self.__height_a
        return print(f'Площадь треугольника равна {S_triangle}')


class Cube(Figure):
    """
        Обладает следующими атрибутами и методами:
        Все атрибуты и методы класса Figure.
        Переопределяет __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
        Метод get_volume, возвращает объём куба.
    """
    sides_count = 12

    def get_sides(self):
        return self.__sides

    def __init__(self, colors, *args):
        super().__init__()
        self.r = colors[0]
        self.g = colors[1]
        self.b = colors[2]
        self.__color = list(colors)
        # print(self.__color)
        self.len_sides = args[0]
        if len(args) > 1:
            self.len_sides = 1
        self.__sides = [self.len_sides] * self.sides_count
        # print(self.__dict__)



    def get_color(self):
        """
        Возвращает список RGB цветов.
        """
        return self.__color

    def get_volume(self):
        self.volume_cub = self.len_sides ** 3
        return self.volume_cub



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
circle1.set_sides(15) # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
#
# Проверка объёма (куба):
print(cube1.get_volume())

# Дополнительная проверка:
# circle2 = Circle((200, 200, 100), 10, 15, 6)  # выдаст ошибку, т.к. принимает только одну сторону
triangle1 = Triangle((200, 200, 100), 10) # условия для треугольника усложнены)))))
triangle2 = Triangle((200, 200, 100), 10, 14, 16)
triangle3 = Triangle((200, 200, 100), 10, 14)
print(triangle1.get_square())
print(triangle2.get_sides())
print(triangle3.get_sides())
cube2 = Cube((200, 200, 100), 9)  #т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, , 9] (12)
print(cube2.get_sides())
cube3 = Cube((200, 200, 100), 9, 12)  #, т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, ..., 1]
print(cube3.get_sides())