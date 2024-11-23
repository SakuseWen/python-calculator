import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_substrct(self):
        self.assertEqual(self.calc.subtract(6, 3), 3)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
            
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 2), 1)
        self.assertEqual(self.calc.modulo(7, -3), 1)
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)

if __name__ == '__main__':
    unittest.main()