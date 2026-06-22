import unittest
import copy

from lab5 import flood_fill

class TestFloodFill(unittest.TestCase):

    def setUp(self):
        self.grid = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]

    def test_standard_fill(self):
        """Перевірка заливки з точки (3, 9) кольором 'C'"""
        grid_copy = copy.deepcopy(self.grid)
        result = flood_fill(grid_copy, 3, 9, 'C')
        
        self.assertEqual(result[3][9], 'C')
        self.assertEqual(result[1][7], 'C')
        self.assertEqual(result[9][9], 'C')
        
        self.assertEqual(result[0][0], 'Y')
        self.assertEqual(result[4][1], 'R')

    def test_same_color(self):
        """Перевірка заливки тим самим кольором (матриця не має змінитись)"""
        grid_copy = copy.deepcopy(self.grid)
        result = flood_fill(grid_copy, 0, 0, 'Y')
        self.assertEqual(result, self.grid)

    def test_isolated_cell(self):
        """Перевірка заливки однієї ізольованої клітинки"""
        small_grid = [
            ['R', 'R', 'R'],
            ['R', 'B', 'R'],
            ['R', 'R', 'R']
        ]
        expected_grid = [
            ['R', 'R', 'R'],
            ['R', 'G', 'R'],
            ['R', 'R', 'R']
        ]
        result = flood_fill(small_grid, 1, 1, 'G')
        self.assertEqual(result, expected_grid)

if __name__ == '__main__':
    unittest.main()