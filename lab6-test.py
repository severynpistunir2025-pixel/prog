import unittest
import os
from lab6 import main

class TestGameServerLatency(unittest.TestCase):
    
    def setUp(self):
        self.cleanup_files()

    def tearDown(self):
        self.cleanup_files()

    def cleanup_files(self):
        for filename in ('gamsrv.in', 'gamsrv.out'):
            if os.path.exists(filename):
                os.remove(filename)

    def run_test_case(self, input_data: str, expected_output: str):
        with open('gamsrv.in', 'w') as fin:
            fin.write(input_data.strip())
            
        main()
        
        self.assertTrue(os.path.exists('gamsrv.out'), "Вихідний файл gamsrv.out не було створено!")
        
        with open('gamsrv.out', 'r') as fout:
            actual_output = fout.read().strip()

        self.assertEqual(actual_output, expected_output)


    def test_example_1(self):
        input_data = """
6 6
1 2 6
1 3 10
3 4 80
4 5 50
5 6 20
2 3 40
2 4 100
        """
        self.run_test_case(input_data, "100")

    def test_example_2(self):
        input_data = """
9 12
2 4 6
1 2 20
2 3 20
3 6 20
6 9 20
9 8 20
8 7 20
7 4 20
4 1 20
5 2 10
5 4 10
5 6 10
5 8 10
        """
        self.run_test_case(input_data, "10")

    def test_example_3(self):
        input_data = """
3 2
1 3
1 2 50
2 3 1000000000
        """
        self.run_test_case(input_data, "1000000000")

    
    def test_empty_input(self):
        """Перевірка поведінки програми при порожньому файлі."""
        input_data = ""
        with open('gamsrv.in', 'w') as fin:
            fin.write(input_data)
        
        main()
        self.assertFalse(os.path.exists('gamsrv.out'), "Для порожнього входу файл gamsrv.out не має створюватися")

if __name__ == '__main__':
    unittest.main()