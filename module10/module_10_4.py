# -*- coding: utf-8 -*-

# Домашнее задание по теме "Очереди для обмена данными между потоками."
# Цель задания:
#
# Освоить механизмы создания потоков и очередей для обмена данных между ними в Python.
# Практически применить знания, создав и запустив несколько потоков и очередь.
#
# Задание:
# Моделирование работы сети кафе с несколькими столиками и потоком посетителей,
# прибывающих для заказа пищи и уходящих после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и уходят
# Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
#
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола,
# is_busy(bool) - занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов,
# в случае наличия стола - начинает обслуживание посетителя (запуск потока),
# в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)

from threading import Thread, Lock
import queue
from time import sleep
import threading


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Customer(Thread):
    def __init__(self, number, table, que=None):
        threading.Thread.__init__(self)
        self.number = number
        self.table = table
        self.que = que

    def run(self):
        print(f"Посетитель номер {self.number} прибыл")

        if self.que == 1:
            print(f"Посетитель номер {self.number} ожидает свободный стол")
            sleep(0.1)

        self.table.is_busy = True
        print(f"Посетитель номер {self.number} сел за стол {self.table.number} (начало обслуживания)")
        sleep(5)
        print(f"Посетитель номер {self.number} покушал и ушёл (конец обслуживания)")
        sleep(0.1)
        self.table.is_busy = False


class Cafe:

    def __init__(self, tables):
        self.queue = queue.Queue(maxsize=1)
        self.tables = tables

    def customer_arrival(self):
        customer_max = 20
        customer = 0
        while customer < customer_max:
            customer += 1
            Cafe.serve_customer(self, customer)
            sleep(1)

    def serve_customer(self, customer):
        table_free = None
        for j in self.tables:
            if not j.is_busy:
                table_free = j
                break

        if table_free:
            customer1 = Customer(customer, table_free)
            customer1.start()
                # customer1.join()
        else:
            self.queue.put(customer)
            # print(f"Посетитель номер {customer} ожидает свободный стол")
            sleep(4)
            table_free1 = None
            for i in self.tables:
                if not i.is_busy:
                    table_free1 = i
                    break
            self.queue.get()
            # print(customer)
            customer2 = Customer(customer, table_free1, que=1)
            customer2.start()


# Создаем столики в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()