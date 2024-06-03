# Ваша задача:
#   Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
#   Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
#   Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
#   Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self):
        self.h_pow = 0
        return ('Мощность двигателя :', self.h_pow)

class Nissan(Car, Vehicle):
    vehicle_type = "Легковой"
    price = 1300000

    def horse_powers(self):
        self.h_pow = 140
        print('Мощность двигателя моего автомобиля', self.__class__.__name__, ":", self.h_pow, 'л/с')



my_car=Nissan
print(my_car.vehicle_type)
print(my_car.price)




