from .datafield import DataField

class DataRecord:
    def __init__(self):
        self.data : list[DataField] = []

    def name_string(self):
        return ', '.join(list(map(lambda x: x.name, self.data)))

    def value_string(self):
        return ', '.join(list(map(lambda x: str(x.data), self.data)))