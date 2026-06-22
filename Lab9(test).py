import unittest

from Lab9 import rabin_karp_all_occurrences

class TestRabinKarp(unittest.TestCase):
    def test_standard_match(self):
        self.assertEqual(rabin_karp_all_occurrences("абарабакарабаба", "раба"), [3, 9])

    def test_multiple_matches(self):
        self.assertEqual(rabin_karp_all_occurrences("aaaaa", "aa"), [0, 1, 2, 3])

    def test_no_match(self):
        self.assertEqual(rabin_karp_all_occurrences("abcdef", "xyz"), [])

    def test_empty_needle(self):
        self.assertEqual(rabin_karp_all_occurrences("abcdef", ""), [])

    def test_needle_longer_than_haystack(self):
        self.assertEqual(rabin_karp_all_occurrences("abc", "abcdef"), [])

    def test_exact_match(self):
        self.assertEqual(rabin_karp_all_occurrences("python", "python"), [0])

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)