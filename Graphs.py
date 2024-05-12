import json
import matplotlib.pyplot as plt


class BarChart:
    def __init__(self):
        self.data = {}
        self.filename = 'numbers.json'

    def data_load(self):
        try:
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            print("Error: Couldn't load data from the JSON file.")
            self.data = {}

    def plot(self):
        algorithms = list(self.data.keys())
        times = list(self.data.values())

        plt.figure(figsize=(12, 8))
        plt.bar(algorithms, times, color='red')
        plt.xlabel('Sorting Algorithm')
        plt.ylabel('Time (seconds)')
        plt.title('Time Taken by Sorting Algorithms')
        plt.xticks(rotation=45, ha='right')
        plt.ylim(0, max(times) / 100)
        plt.tight_layout()
        plt.show()

    def clear(self):
        with open(self.filename, 'w') as f:
            f.write('{}')