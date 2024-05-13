## Coursework Report

### 1. Introduction

- **Application**: The application is a Python program that implements various sorting algorithms and exports the execution time of each algorithm to a JSON file.
- **How to run the program**: The program can be run by executing the main Python script containing the sorting algorithms and the ExportJson class.
- **How to use the program**: Users can import the sorting algorithms they need from the main script or create their own instances. They can then call the `sort()` method on these instances to sort their input arrays. The execution time of each algorithm will be recorded in a JSON file.

### 2. Body/Analysis

- **Functional requirements**: The program covers functional requirements by providing implementations of various sorting algorithms such as Selection Sort, Insertion Sort, Quick Sort, etc. It ensures that each algorithm correctly sorts the input array and records the execution time accurately.

```python
# Example usage of the program
from SortAlgorithms import SelectionSort, ExportJson

arr_unsorted = [-10, -30, 0, 13, -1, 34, 5, 2, 9, 10]

# Using Selection Sort algorithm
selection_sort = SelectionSort(arr_unsorted)
selection_sort.sort()

# JSON file will contain execution time of the algorithm
```

### 3. Results and Summary

- **Results**: The program successfully implements and tests various sorting algorithms. Challenges faced during implementation include ensuring correct algorithm implementations and handling JSON file writing.
- **Conclusions**: The program achieves its goal of providing implementations of sorting algorithms and recording their execution times. It demonstrates good extensibility by allowing easy addition of new sorting algorithms and further functionality.

```python
# Example test case for JSON file writing
from SortAlgorithms import ExportJson

# Test adding a record to JSON file
export_json = ExportJson()
export_json.add_record('bubble sort', 0.005)
```

### 4. Future Prospects

- **Program Result**: The result of the program is a JSON file containing the execution times of each sorting algorithm.
- **Future Prospects**: The program could be extended by adding more sorting algorithms or by implementing additional functionality, such as visualization of sorting algorithms or parallel execution of sorting tasks for large datasets.
