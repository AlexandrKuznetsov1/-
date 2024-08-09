# -*- coding: utf-8 -*-

import runner
import runner_and_tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        walker = runner.Runner('walker')
        for _ in range(10):
            walker.walk()
        a = getattr(walker, "distance")
        self.assertEqual(a, 50)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner1 = runner.Runner('runner1')
        for _ in range(10):
            runner1.run()
        b = getattr(runner1, "distance")
        self.assertEqual(b, 100)

    @unittest.skipIf(False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        walker1 = runner.Runner('walker1')
        runner2 = runner.Runner('runner2')
        for _ in range(10):
            walker1.walk()
            runner2.run()
        c = getattr(walker1, "distance")
        d = getattr(runner2, "distance")
        self.assertNotEqual(c, d)


if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.list_runners = ['Усэйн', 'Андрей', 'Ник']
        self.runner1 = runner_and_tournament.Runner(self.list_runners[0], 10)
        self.runner2 = runner_and_tournament.Runner(self.list_runners[1], 9)
        self.runner3 = runner_and_tournament.Runner(self.list_runners[2], 3)

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_race1(self):
        """
        Так как в забеге 2 участника, достаточно сравнить результат только проигравшего
        """
        race1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.results = race1.start()
        self.assertTrue(self.results.get(2), self.list_runners[-1])
        self.all_results[1] = self.list_runners[0]
        self.all_results[2] = self.list_runners[-1]

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_race2(self):
        race2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.results = race2.start()
        self.assertTrue(self.results.get(2), self.list_runners[-1])
        self.all_results[1] = self.list_runners[1]
        self.all_results[2] = self.list_runners[-1]

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
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

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def tearDown(self):
        print(self.all_results)

    @classmethod
    def tearDownClass(cls):
        # print("Вывод на консоль по третьему забегу,- отраженный в задании {1: Андрей, 2: Усэйн, 3: Ник} НЕКОРРЕКТНЫЙ")
        # print("Андрей по условию никогда не может быть первым")
        print("Все получилось")