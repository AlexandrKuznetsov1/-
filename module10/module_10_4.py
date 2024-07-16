# -*- coding: utf-8 -*-

# "Многопроцессное программирование"
# Цель задания:
#
# Освоить механизмы создания процессов в Python.
# Практически применить знания, создав несколько параллельных процессов и запустив их.
#
# Задание:
# Моделирование программы для управления данными о движении товаров на складе и эффективной обработки запросов
# на обновление информации в многопользовательской среде.
#
# Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на обновление информации
# о поступлении товаров и отгрузке товаров.
# Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти запросы
# в многопользовательской среде, с использованием механизма мультипроцессорности для обеспечения
# быстрой реакции на поступающие данные.
#
# Создайте класс WarehouseManager - менеджера склада, который будет обладать следующими свойствами:
# Атрибут data - словарь, где ключ - название продукта, а значение - его кол-во. (изначально пустой)
# Метод process_request - реализует запрос (действие с товаром), принимая request - кортеж.
# Есть 2 действия: receipt - получение, shipment - отгрузка.
# а) В случае получения данные должны поступить в data (добавить пару, если её не было и изменить значение ключа,
# если позиция уже была в словаре)
# б) В случае отгрузки данные товара должны уменьшаться (если товар есть в data и если товара больше чем 0).
#
# Метод run - принимает запросы и создаёт для каждого свой параллельный процесс,
# запускает его(start) и замораживает(join).


import multiprocessing
from colorama import Fore, init
init(autoreset=True)
from time import sleep


class WarehouseManager:
    data = {}

    def process_request(self, *request):
        lock = request[-1]
        lock.acquire()


                # print(new_request)
        try:

            for i in request[0]:
                for j in i:
                    current_request = j[1]
                    name_product = j[0]
                    quantity_product = j[-1]
                    if current_request == 'receipt':
                        if name_product not in self.data:
                            self.data[name_product] = quantity_product
                        else:
                            self.data[name_product] += quantity_product
                        # print(self.data)

                    if current_request == "shipment":
                        if name_product not in self.data:
                            self.data[name_product] = quantity_product
                        if self.data[name_product] >= quantity_product:
                            self.data[name_product] -= quantity_product
            # print(self.data)
        finally:
            sleep(1)
            print(Fore.BLUE + 'Поэтому возвращаем сразу после окончания работы процесса из метода')
            sleep(1)
            print(Fore.RED + str(self.data))
            sleep(1)

            lock.release()


    def run(self, *args):
        lock = multiprocessing.Lock()
        if __name__ == '__main__':
            process = multiprocessing.Process(target=self.process_request, args=(args, lock))
            process.start()
            process.join()


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests)

# Выводим обновленные данные о складских запасах
print(f'так как изначально атрибут data = пустой{manager.data} и по завершении процессов остается {'{}'} manager.data'
      f' возвращает {'{}'} чтобы получить данный результат необходимо self.data передать в глобальную переменную')
