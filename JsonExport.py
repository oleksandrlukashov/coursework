import json


class ExportJson:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.filename = 'numbers.json'

    def add_record(self, algorithm, time_taken):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = {}
        data[algorithm] = time_taken
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
