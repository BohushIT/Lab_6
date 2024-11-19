import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Ініціалізуємо екземпляр калькулятора перед кожним тестом
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(3, 5), 8)
        self.assertEqual(self.calculator.add(-1, 1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)


    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)


    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 5), 15)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)



    def test_parse_input_invalid(self):
        # Перевірка неправильного введення
        with self.assertRaises(ValueError):
            self.calculator.parse_input("2+1")

        with self.assertRaises(ValueError):
            self.calculator.parse_input("2_1")

        with self.assertRaises(ValueError):
            self.calculator.parse_input("abc")

        with self.assertRaises(ValueError):
            self.calculator.parse_input("12a")

        with self.assertRaises(ValueError):
            self.calculator.parse_input("!@#")
        with self.assertRaises(ValueError):
            self.calculator.parse_input("")

        with self.assertRaises(ValueError):
            self.calculator.parse_input("3.14.15")

        self.assertEqual(self.calculator.parse_input("3"),3)



    def test_divide(self):
        self.assertEqual(self.calculator.divide(10, 2), 5)
        # Перевірка винятку при діленні на нуль
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0);



