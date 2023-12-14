import unittest

from find_min_unsorted_subarray import find_min_unsorted_subarray_n


class TestFindMinUnsortedSubarray(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        result = find_min_unsorted_subarray_n(arr, False)
        self.assertEqual((-1, -1), result)

    def test_unsorted_array(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        result = find_min_unsorted_subarray_n(arr, False)
        self.assertEqual((3, 9), result)

    def test_unsorted_array_reversed(self):
        arr = [12, 11, 10, 4, 9, 8, 7, 6, 5, 3, 2, 1]
        result = find_min_unsorted_subarray_n(arr, True)
        self.assertEqual((3, 8), result)

    def test_one_element_array(self):
        arr = [1]
        result = find_min_unsorted_subarray_n(arr, False)
        self.assertEqual((-1, -1), result)


if __name__ == "__main__":
    unittest.main()
