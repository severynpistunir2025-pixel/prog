import unittest
from lab1 import is_subarray

class TestIsSubarray(unittest.TestCase):
    
    def test_case_1(self):
        # nums1 = [1, 2, 3], nums2 = [1, 2, 3, 4] -> True
        self.assertTrue(is_subarray([1, 2, 3], [1, 2, 3, 4]))
        
    def test_case_2(self):
        # nums1 = [4, 2], nums2 = [1, 2, 3, 4] -> False
        self.assertFalse(is_subarray([4, 2], [1, 2, 3, 4]))
        
    def test_case_3(self):
        # nums1 = [1, 3, 5], nums2 = [1, 2, 3, 4, 5] -> True
        self.assertTrue(is_subarray([1, 3, 5], [1, 2, 3, 4, 5]))

    def test_empty_first(self):
        self.assertTrue(is_subarray([], [1, 2, 3]))

    def test_not_present(self):
        self.assertFalse(is_subarray([10], [1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
    