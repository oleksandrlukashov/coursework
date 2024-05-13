from copy import copy
from abc import ABC
import time
import JsonExport


class Sort(ABC):

    def __init__(self, arr):
        self._arr = arr
        self._arr_to_be_sorted = []
        self._length = int(len(self._arr))
        self.name = ''
        self.time_taken = None

    @staticmethod
    def _time_print(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            self._arr_to_be_sorted = copy(self._arr)
            start = time.time()
            func(*args, **kwargs)
            stop = time.time()
            print(f'Given array: {self._arr}')
            print(f'Array sorted using {self.name} method: {self._arr_to_be_sorted}')
            print(stop - start, '\n')
            self.time_taken = stop - start
            singleton = JsonExport.ExportJson()
            singleton.add_record(self.name, self.time_taken)

        return wrapper


class SelectionSort(Sort):
    @Sort._time_print
    def sort(self):
        self.name = 'selection sort'
        for i in range(self._length):
            min_index = i
            for j in range(i + 1, self._length):
                if self._arr_to_be_sorted[j] < self._arr_to_be_sorted[min_index]:
                    min_index = j
            (self._arr_to_be_sorted[i], self._arr_to_be_sorted[min_index]) = (
                self._arr_to_be_sorted[min_index], self._arr_to_be_sorted[i])


class InsertionSort(Sort):
    @Sort._time_print
    def sort(self):
        self.name = 'insertion sort'
        if self._length <= 1:
            return self._arr_to_be_sorted
        for i in range(1, self._length):
            key = self._arr_to_be_sorted[i]
            j = i - 1
            while j >= 0 and key < self._arr_to_be_sorted[j]:
                self._arr_to_be_sorted[j + 1] = self._arr_to_be_sorted[j]
                j -= 1
            self._arr_to_be_sorted[j + 1] = key


class BuiltinSort(Sort):
    @Sort._time_print
    def sort(self):
        self.name = 'built-in "sort"'
        self._arr_to_be_sorted.sort()


class BuiltInSorted(Sort):
    @Sort._time_print
    def sort(self):
        self.name = 'built-in "sorted"'
        self._arr_to_be_sorted = sorted(self._arr)


class BubbleSort(Sort):
    @Sort._time_print
    def sort(self):
        self.name = 'bubble sort'
        if self._length == 1 or self._length == 0:
            return self._arr
        for i in range(self._length):
            for j in range(0, self._length - i - 1):
                if self._arr_to_be_sorted[j] > self._arr_to_be_sorted[j + 1]:
                    temp = self._arr_to_be_sorted[j]
                    self._arr_to_be_sorted[j] = self._arr_to_be_sorted[j + 1]
                    self._arr_to_be_sorted[j + 1] = temp


class QuickSort(Sort):
    @staticmethod
    def __partition(nlist, low, high):
        pivot = nlist[high]
        i = low - 1
        for j in range(low, high):
            if nlist[j] <= pivot:
                i = i + 1
                (nlist[i], nlist[j]) = (nlist[j], nlist[i])
        (nlist[i + 1], nlist[high]) = (nlist[high], nlist[i + 1])
        return i + 1

    def __quick_sort_(self, nlist, low, high):
        if low < high:
            pi = self.__partition(nlist, low, high)
            self.__quick_sort_(nlist, low, pi - 1)
            self.__quick_sort_(nlist, pi + 1, high)

    @Sort._time_print
    def sort(self):
        self.name = 'quick sort'
        self.__quick_sort_(self._arr_to_be_sorted, 0, len(self._arr_to_be_sorted) - 1)


class ShellSort(Sort):

    @Sort._time_print
    def sort(self):
        self.name = 'shell sort'
        delta = self._length // 2
        while delta > 0:
            for i in range(int(delta), self._length):
                temp = self._arr_to_be_sorted[i]
                j = i
                while j >= int(delta) and self._arr_to_be_sorted[j - int(delta)] > temp:
                    self._arr_to_be_sorted[j] = self._arr_to_be_sorted[j - int(delta)]
                    j -= int(delta)
                self._arr_to_be_sorted[j] = temp
            delta /= 2


class CombSort(Sort):

    @staticmethod
    def next_gap(gap):
        gap = (gap * 10) / 13
        if gap < 1:
            return 1
        return gap

    @Sort._time_print
    def sort(self):
        self.name = 'comb sort'
        gap = self._length
        swapped = True
        while int(gap) != 1 or swapped == 1:
            gap = self.next_gap(int(gap))
            swapped = False
            for i in range(0, self._length - int(gap)):
                if self._arr_to_be_sorted[i] > self._arr_to_be_sorted[i + int(gap)]:
                    self._arr_to_be_sorted[i], self._arr_to_be_sorted[i + int(gap)] = self._arr_to_be_sorted[
                        i + int(gap)], self._arr_to_be_sorted[i]
                    swapped = True
