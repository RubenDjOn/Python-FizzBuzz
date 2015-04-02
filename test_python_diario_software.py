import unittest

import python_diario


class TestPythonSoftware(unittest.TestCase):

    def test_should_return_python_when_number_is_divisble_by_3(self):
        self.assertEqual('Python', python_diario.get_string(3))

    def test_should_return_python_when_number_is_divisble_by_6(self):
        self.assertEqual('Python', python_diario.get_string(6))

    def test_should_return_python_when_number_is_divisble_by_9(self):
        self.assertEqual('Python', python_diario.get_string(9))

    def test_should_return_diario_when_number_is_divisble_by_5(self):
        self.assertEqual('Diario', python_diario.get_string(5))

    def test_should_return_diario_when_number_is_divisble_by_10(self):
        self.assertEqual('Diario', python_diario.get_string(10))

    def test_should_return_diario_when_number_is_divisble_by_20(self):
        self.assertEqual('Diario', python_diario.get_string(20))

    def test_should_return_7_when_number_is_7(self):
        self.assertEqual(7, python_diario.get_string(7))

    def test_should_return_11_when_number_is_11(self):
        self.assertEqual(11, python_diario.get_string(11))

    def test_should_return_41_when_number_is_41(self):
        self.assertEqual(41, python_diario.get_string(41))

if __name__ == '__main__':
    unittest.main()
