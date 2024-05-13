import random
import Algorithms
import Graphs


class RandInts:
    def __init__(self):
        self.arr = []

    def algorithms_grpah(func):
        def wrapper(*args, **kwargs):
            self = args[0]
            self.arr = []
            func(*args, **kwargs)
            selection_sort = Algorithms.SelectionSort(self.arr)
            insertion_sort = Algorithms.InsertionSort(self.arr)
            builtinsort = Algorithms.BuiltinSort(self.arr)
            builtinsorted = Algorithms.BuiltInSorted(self.arr)
            bubble_sort = Algorithms.BubbleSort(self.arr)
            quick_sort = Algorithms.QuickSort(self.arr)
            shell_sort = Algorithms.ShellSort(self.arr)
            comb_sort = Algorithms.CombSort(self.arr)
            selection_sort.sort()
            insertion_sort.sort()
            builtinsort.sort()
            builtinsorted.sort()
            bubble_sort.sort()
            quick_sort.sort()
            shell_sort.sort()
            comb_sort.sort()
            graphs = Graphs.BarChart()
            graphs.data_load()
            graphs.plot()
            graphs.clear()
        return wrapper

    @algorithms_grpah
    def generate_10(self):
        self.arr = [random.randint(1, 1000) for _ in range(10)]

    @algorithms_grpah
    def generate_50(self):
        self.arr = [random.randint(1, 1000) for _ in range(50)]

    @algorithms_grpah
    def generate_100(self):
        self.arr = [random.randint(1, 1000) for _ in range(100)]

    @algorithms_grpah
    def generate_200(self):
        self.arr = [random.randint(1, 1000) for _ in range(200)]

    @algorithms_grpah
    def generate_500(self):
        self.arr = [random.randint(1, 1000) for _ in range(500)]

    @algorithms_grpah
    def generate_1000(self):
        self.arr = [random.randint(1, 1000) for _ in range(1000)]


exe = RandInts()
exe.generate_10()
exe.generate_50()
exe.generate_100()
exe.generate_200()
exe.generate_500()
