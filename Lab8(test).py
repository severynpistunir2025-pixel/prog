import unittest
from Lab8 import calculate_paths

class TestIJones(unittest.TestCase):

    def test_example_1(self):
        W, H = 3, 3
        matrix = [
            "aaa",
            "cab",
            "def"
        ]
        self.assertEqual(calculate_paths(W, H, matrix), 5)

    def test_example_2(self):
        W, H = 10, 1
        matrix = ["abcdefaghi"]
        self.assertEqual(calculate_paths(W, H, matrix), 2)

    def test_example_3(self):
        W, H = 7, 6
        matrix = ["aaaaaaa"] * 6
        self.assertEqual(calculate_paths(W, H, matrix), 201684)

    def test_minimal_case(self):
        W, H = 1, 1
        matrix = ["a"]
        self.assertEqual(calculate_paths(W, H, matrix), 1)

if __name__ == '__main__':
    unittest.main()