import unittest
from FizzBuzz import FizzBuzz


class MyTestCase(unittest.TestCase):

    def test_number_divide_by_3_fizz(self):
        self.assertEqual(FizzBuzz(3).fizz_buzz(), "Fizz")

    def test_number_divide_by_5_buzz(self):
        self.assertEqual(FizzBuzz(5).fizz_buzz(), "Buzz")

    def test_number_divide_by_3_and_5_fizzbuzz(self):
        self.assertEqual(FizzBuzz(15).fizz_buzz(), "FizzBuzz")

    def test_number_divide_by_2_number(self):
        self.assertEqual(FizzBuzz(2).fizz_buzz(), "2")

if __name__ == '__main__':
    unittest.main()
