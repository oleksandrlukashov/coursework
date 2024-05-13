import unittest
from Algorithms import *


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.arr_unsorted = [-10, -30, 0, 13, -1, 34, 5, 2, 9, 10]
        self.sorted_arr = [-30, -10, -1, 0, 2, 5, 9, 10, 13, 34]

    def test_selection_sort(self):
        selection_sort = SelectionSort(self.arr_unsorted)
        selection_sort.sort()
        self.assertEqual(selection_sort._arr_to_be_sorted, self.sorted_arr)

    def test_insertion_sort(self):
        insertion_sort = InsertionSort(self.arr_unsorted)
        insertion_sort.sort()
        self.assertEqual(insertion_sort._arr_to_be_sorted, self.sorted_arr)

    def test_builtin_sort(self):
        builtin_sort = BuiltinSort(self.arr_unsorted)
        builtin_sort.sort()
        self.assertEqual(builtin_sort._arr_to_be_sorted, self.sorted_arr)

    def test_builtin_sorted(self):
        builtin_sorted = BuiltInSorted(self.arr_unsorted)
        builtin_sorted.sort()
        self.assertEqual(builtin_sorted._arr_to_be_sorted, self.sorted_arr)

    def test_bubble_sort(self):
        bubble_sort = BubbleSort(self.arr_unsorted)
        bubble_sort.sort()
        self.assertEqual(bubble_sort._arr_to_be_sorted, self.sorted_arr)

    def test_quick_sort(self):
        quick_sort = QuickSort(self.arr_unsorted)
        quick_sort.sort()
        self.assertEqual(quick_sort._arr_to_be_sorted, self.sorted_arr)

    def test_shell_sort(self):
        shell_sort = ShellSort(self.arr_unsorted)
        shell_sort.sort()
        self.assertEqual(shell_sort._arr_to_be_sorted, self.sorted_arr)

    def test_comb_sort(self):
        comb_sort = CombSort(self.arr_unsorted)
        comb_sort.sort()
        self.assertEqual(comb_sort._arr_to_be_sorted, self.sorted_arr)


if __name__ == '__main__':
    unittest.main()
