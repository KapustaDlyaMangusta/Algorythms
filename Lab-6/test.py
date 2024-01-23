import unittest
from kmp_algorythm import kmp_search


class TestKMPAlgorithm(unittest.TestCase):

    def test_kmp_search_basic(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        result = kmp_search(haystack, needle)
        self.assertEqual(result, [2, 7, 10, 13])

    def test_kmp_search_no_occurrence(self):
        haystack = "abcdefgh"
        needle = "xyz"
        result = kmp_search(haystack, needle)
        self.assertEqual(result, [])

    def test_kmp_search_empty_needle(self):
        haystack = "abab"
        needle = ""
        result = kmp_search(haystack, needle)
        self.assertEqual(result, [0, 1, 2, 3, 4])

    def test_kmp_search_long_needle(self):
        haystack = "abracadabra"
        needle = "abracadabra"
        result = kmp_search(haystack, needle)
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()
