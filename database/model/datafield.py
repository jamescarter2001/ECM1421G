from .fieldtype import FieldType

class DataField:
    def __init__(self, name, data, field_type : FieldType = FieldType.string):
        self.name = name

        if field_type == FieldType.number:
            self.data = data
        elif field_type == FieldType.string:
            self.data = f"'{data}'"