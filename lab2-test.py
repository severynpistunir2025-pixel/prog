import unittest
from lab2 import get_optimal_price
class TestDiscountSystem(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(get_optimal_price([50, 20, 30, 17, 100], 10), "207.00")

    def test_case_2(self):
        self.assertEqual(get_optimal_price([1, 2, 3, 4, 5, 6, 7], 100), "15.00")

    def test_case_3(self):
        self.assertEqual(get_optimal_price([1, 1, 1], 33), "2.67")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)                                                                            