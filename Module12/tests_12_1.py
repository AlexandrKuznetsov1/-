# -*- coding: utf-8 -*-


# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:

# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод walk у этого объекта 10 раз. После чего методом assertEqual
# сравните distance этого объекта со значением 50.

# test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
# Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual
# сравните distance этого объекта со значением 100.

# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
# Далее 10 раз у объектов вызываются методы run и walk соответственно.
# Т.к. дистанции должны быть разными, используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.

# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку.

import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('walker')
        for _ in range(10):
            walker.walk()
        a = getattr(walker, "distance")
        self.assertEqual(a, 50)

    def test_run(self):
        runner1 = runner.Runner('runner1')
        for _ in range(10):
            runner1.run()
        b = getattr(runner1, "distance")
        self.assertEqual(b, 100)

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
