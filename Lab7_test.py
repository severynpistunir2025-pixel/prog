import unittest
import os
import csv
from Lab7 import prim_mst_length, read_matrix_from_csv

class TestVeniceCable(unittest.TestCase):
    def setUp(self):
        """Створює тимчасовий CSV файл перед кожним тестом для перевірки зчитування."""
        self.test_csv_path = "test_islands.csv"
        self.test_data = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0],
        ]
        with open(self.test_csv_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(self.test_data)

    def tearDown(self):
        """Видаляє тимчасовий файл після виконання тесту."""
        if os.path.exists(self.test_csv_path):
            os.remove(self.test_csv_path)

    def test_prim_mst_basic(self):
        """Тестування стандартної матриці суміжності."""
        # Очікувані ребра: (0-1: 2), (1-2: 3), (1-4: 5), (0-3: 6). Сума = 16
        self.assertEqual(prim_mst_length(self.test_data), 16)

    def test_disconnected_graph(self):
        """Тестування незв'язного графа (має повернути -1)."""
        matrix = [
            [0, 2, 0],
            [2, 0, 0],
            [0, 0, 0] # Острів без зв'язків
        ]
        self.assertEqual(prim_mst_length(matrix), -1)

    def test_single_island(self):
        """Тестування з одним островом."""
        matrix = [[0]]
        self.assertEqual(prim_mst_length(matrix), 0)

    def test_csv_reader(self):
        """Тестування правильності зчитування даних з CSV."""
        matrix = read_matrix_from_csv(self.test_csv_path)
        self.assertEqual(len(matrix), 5)
        self.assertEqual(matrix[0][1], 2)
        self.assertEqual(matrix[4][2], 7)

if __name__ == "__main__":
    unittest.main()