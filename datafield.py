class DataField:
    def __init__(self, name, data, is_number = False):
        self.name = name

        if is_number:
            self.data = data
        else:
            self.data = f"'{data}'"