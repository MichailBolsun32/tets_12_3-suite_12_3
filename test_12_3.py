import runner_and_tournament
import unittest

# Напишите класс TournamentTest, наследованный от TestCase.
class TournamentTest(unittest.TestCase):
# setUpClass - метод, где создаётся атрибут класса all_results.
#       Это словарь в который будут сохраняться результаты всех тестов.
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        
# setUp - метод, где создаются 3 объекта:
#
#     Бегун по имени Усэйн, со скоростью 10.
#     Бегун по имени Андрей, со скоростью 9.
#     Бегун по имени Ник, со скоростью 3.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run_Yce = runner_and_tournament.Runner('Усэйн', 10)
        self.run_And = runner_and_tournament.Runner('Андрей', 9)
        self.run_Nik = runner_and_tournament.Runner('Ник', 3)
# Так же методы тестирования забегов, в которых создаётся объект Tournament
# на дистанцию 90. У объекта класса Tournament запускается метод start,
# который возвращает словарь в переменную all_results.
# В конце вызывается метод assertTrue, в котором сравниваются последний объект
# из all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
# Напишите 3 таких метода, где в забегах участвуют
# (порядок передачи в объект Tournament соблюсти):
#
#     Усэйн и Ник
#     Андрей и Ник
#     Усэйн, Андрей и Ник.
#
# Как можно понять: Ник всегда должен быть последним.
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        tournament = runner_and_tournament.Tournament(90, self.run_Yce, self.run_Nik)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == 'Ник')


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        tournament = runner_and_tournament.Tournament(90, self.run_And, self.run_Nik)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == 'Ник')


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        tournament = runner_and_tournament.Tournament(90, self.run_Yce, self.run_And, self.run_Nik)
        result = tournament.start()
        self.all_results.append(result)
        self.assertTrue(result[max(result.keys())] == 'Ник')

   #tearDownClass - метод, где выводятся all_results по очереди в столбец.
    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            #преобразуем dict к читабельному виду, т.к. Runner поменять не можем
            result_print = {k: str(v) for k, v in result.items()}
            print(result_print)

#  Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest.
#  В классе пропишите следующие методы:

    # test_walk - метод, в котором создаётся объект класса Runner
        # с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз.
        # После чего методом assertEqual сравните distance этого объекта со значением 50.
    # test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        # Далее вызовите метод run у этого объекта 10 раз.
        # После чего методом assertEqual сравните distance этого объекта со значением 100.
    # test_challenge - метод в котором создаются 2 объекта класса Runner с
        # произвольными именами. Далее 10 раз у объектов вызываются методы run и walk
        # соответственно. Т.к. дистанции должны быть разными,
        # используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_wolk(self):
        run_wolk = runner_and_tournament.Runner('Wolk')

        for _ in range(10):
            run_wolk.walk()
        self.assertEqual(run_wolk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        run_run = runner_and_tournament.Runner('Run')

        for _ in range(10):
            run_run.run()
        self.assertEqual(run_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        run_wolk = runner_and_tournament.Runner('Wolk')
        run_run = runner_and_tournament.Runner('Run')

        for _ in range(10):
            run_wolk.walk()
            run_wolk.run()

        for _ in range(9):
            run_run.walk()
            run_run.run()

        self.assertNotEqual(run_wolk.distance, run_run.distance)



if __name__ == '__main__':
    unittest.main()