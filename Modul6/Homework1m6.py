# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
# которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price,
# а также переопределите функцию horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также свойство price,
# а также переопределите функцию horse_powers

class Car:
    """
    Автомобили
    """
    price = 1000000

    def horse_powers(self):
        self.h_pow = 0
        return ('Мощность двигателя :', self.h_pow)

class Nissan(Car):
    """Ниссан, - Наследник класса автомобили"""

    price = 1200000
    def horse_powers(self):
        self.h_pow = 140
        self.angine = "двигатель дизельный"
        print('Мощность двигателя у автомобиля', self.__class__.__name__, ":", self.h_pow, 'л/с ,цена :',
              self.price, 'рублей,-', self.angine)
class Kia(Car):
    """Киа, - Наследник класса автомобили"""

    price = 800000
    def horse_powers(self):
        self.h_pow = 100
        self.angine = "двигатель бензиновый"
        print('Мощность двигателя у автомобиля :', self.__class__.__name__, ":", self.h_pow, 'л/с ,цена :',
              self.price, 'рублей,-', self.angine)

class Zaz(Car):
    """ЗАЗ, - Наследник класса автомобили"""

    price = 10
    def horse_powers(self):
        self.h_pow = 0
        self.angine = "двигатель мертвый"
        self.body = 'кузов гнилой'
        print('Мощность двигателя у автомобиля :', self.__class__.__name__, ":", self.h_pow, 'л/с ,цена :',
              self.price, 'рублей,-', self.angine, ",", self.body)
cars = Car()
print(cars.price)
print(cars.horse_powers())
pulya = Nissan()
pilula = Kia()
pulya.price
pulya.horse_powers()
pilula.price
pilula.horse_powers()
death = Zaz()
death.horse_powers()
death.price
