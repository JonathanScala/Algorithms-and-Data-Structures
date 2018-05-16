import unittest
import sys
import os


class Test_Radix_Sort(unittest.TestCase):

    def test_empty_list(self):
        result = Sorting.radix_sort([])
        self.assertEqual(result, [], "Cannot sort an empty list")

    def test_single_element_list(self):
        result = Sorting.radix_sort([1])
        self.assertEqual(result, [1], "Cannot sort a list with 1 element")

    def test_already_sorted_list(self):
        result = Sorting.radix_sort([1, 2, 3, 4])
        self.assertEqual(result, [1, 2, 3, 4],
                         "Cannot sort a list already in sorted order")

    def test_reverse_sorted_list(self):
        result = Sorting.radix_sort([4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4],
                         "Cannot sort a list in reverse sorted order")

    def test_repeated_element_list(self):
        result = Sorting.radix_sort([1, 3, 2, 1])
        self.assertEqual(result, [1, 1, 2, 3],
                         "Cannot sort a list with repeated elements")

if(__name__ == "__main__"):
    sys.path.append(os.path.abspath('../Algorithms'))
    from Sorts import Sorting
    unittest.main(exit=False)
