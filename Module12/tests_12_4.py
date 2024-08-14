# -*- coding: utf-8 -*-

# Цель: получить опыт использования простейшего логирования совместно с тестами.

# Основное обновление - выбрасывание исключений,
# если передан неверный тип в name и если передано отрицательное значение в speed.
#
# Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
# В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
# Уровень - INFO
# Режим - чтение
# Название файла - runner_tests.log
# Кодировка - UTF-8
# Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
#
# Дополните методы тестирования в классе RunnerTest следующим образом:
# test_walk:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте отрицательное значение в speed.
# В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
# с сообщением "Неверная скорость для Runner".
# test_run:
# Оберните основной код конструкцией try-except.
# При создании объекта Runner передавайте что-то кроме строки в name.
# В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
# В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING
# с сообщением "Неверный тип данных для объекта Runner".

import logging


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        try:
            self.distance += self.speed * 2
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    def walk(self):
        try:
            self.distance += self.speed
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner")


    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


if __name__ == '__main__':
    fileHandler = logging.FileHandler(filename='runner_tests.log', encoding='utf-8')   # Создаем обработчик для записи в файл
    format_rec = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")  # задаем формат записи
    fileHandler.setFormatter(format_rec)  # устанавливаем форматирование в обработчик
    logger = logging.getLogger()   # Получаем корневой логгер
    logger.addHandler(fileHandler)  # Добавляем обработчик к логгеру
    logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования INFO
    # logger.setLevel(logging.WARNING)
    # logging.basicConfig(level=logging.INFO, filemode="r", filename='runner_tests.log', encoding='utf-8',
    #                     format="%(levelname)s -*- %(message)s")

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)
#
t = Tournament(101,  first, second, third)
print(t.start())


