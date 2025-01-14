import unittest
from Factorial import calculate_factorial

class TestFactorialFunction(unittest.TestCase):
      def test_factorial_positive(self):
            self.assertEqual(calculate_factorial(5), 120)
            self.assertEqual(calculate_factorial(3), 6)
            self.assertEqual(calculate_factorial(1), 1)

      def test_factorial_zero(self):
            self.assertEqual(calculate_factorial(0), 1)
      
      def test_factorial_negative(self):
            self.assertIsNone(calculate_factorial(-1))

if __name__ == '__main__':
      unittest.main()