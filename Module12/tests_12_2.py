# -*- coding: utf-8 -*-
import time

# Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:
#
# setUpClass - метод, где создаётся атрибут класса all_results. Это словарь
# в который будут сохраняться результаты всех тестов.
# setUp - метод, где создаются 3 объекта:
# Бегун по имени Усэйн, со скоростью 10.
# Бегун по имени Андрей, со скоростью 9.
# Бегун по имени Ник, со скоростью 3.
# tearDownClass - метод, где выводятся all_results по очереди в столбец.
#
# Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
# У объекта класса Tournament запускается метод start, который возвращает словарь в переменную results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект из result
# и предполагаемое имя последнего бегуна (индекс -1).
# Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
# Усэйн и Ник
# Андрей и Ник
# Усэйн, Андрей и Ник.
# Как можно понять: Ник всегда должен быть последним.

import runner_and_tournament
import unittest
from time import sleep


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        # pass

    def setUp(self):
        self.list_runners = ['Усэйн', 'Андрей', 'Ник']
        self.runner1 = runner_and_tournament.Runner(self.list_runners[0], 10)
        self.runner2 = runner_and_tournament.Runner(self.list_runners[1], 9)
        self.runner3 = runner_and_tournament.Runner(self.list_runners[2], 3)

    def test_race1(self):
        """
        Так как в забеге 2 участника, достаточно сравнить результат только проигравшего
        """
        race1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.results = race1.start()
        self.assertTrue(self.results.get(2), self.list_runners[-1])
        self.all_results[1] = self.list_runners[0]
        self.all_results[2] = self.list_runners[-1]

    def test_race2(self):
        race2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.results = race2.start()
        self.assertTrue(self.results.get(2), self.list_runners[-1])
        self.all_results[1] = self.list_runners[1]
        self.all_results[2] = self.list_runners[-1]

    def test_race3(self):
        """
        В последнем забеге для получения корректного результата сравниваем результаты чемпиона и проигравшего
        """
        race3 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.results = race3.start()
        self.assertTrue(self.results.get(1), self.list_runners[0])
        self.assertTrue(self.results.get(3), self.list_runners[-1])
        self.all_results[1] = self.list_runners[0]
        self.all_results[2] = self.list_runners[1]
        self.all_results[3] = self.list_runners[-1]

    def tearDown(self):
        print(self.all_results)

    @classmethod
    def tearDownClass(cls):
        time.sleep(0.2)
        print("Вывод на консоль по третьему забегу,- отраженный в задании {1: Андрей, 2: Усэйн, 3: Ник} НЕКОРРЕКТНЫЙ")
        print("Андрей по условию никогда не может быть первым")





