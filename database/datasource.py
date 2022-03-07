from typing import TypeVar, Generic

from .model.operationtype import OperationType

from .model.datarecord import DataRecord

T = TypeVar('T')

class DataSource(Generic[T]):
    def __init__(self, connection_context, table_name):
        self.table_name = table_name
        self.context = connection_context

        self.subscribers = []
        
        self.data : dict[int, T] = {}

        self.load_data()

    def subscribe(self, func):
        self.subscribers.append(func)

    def onCreateOrUpdate(self, model : T):
        for sub in self.subscribers:
            sub(model, OperationType.update)

    def onDelete(self, model : T):
        for sub in self.subscribers:
            sub(model, OperationType.delete)

    def create_model(self, row) -> T:
        raise NotImplementedError

    def create_record(self, model : T) -> DataRecord:
        raise NotImplementedError

    def get_for_id(self, id):
        return self.data[id]

    def load_data(self):

        query = f"SELECT * FROM {self.table_name}"
        print(query)
        self.context.cursor.execute(query)
        row = self.context.cursor.fetchone()

        while row:
            model : T = self.create_model(row)
            self.data[model.id] = model
            row = self.context.cursor.fetchone()

    def add(self, model : T):
        r : DataRecord = self.create_record(model, new=True if model.id == 0 else False)

        name_string = ', '.join(list(map(lambda x: x.name, r.data)))
        value_string = ', '.join(list(map(lambda x: str(x.data), r.data)))

        query = f"INSERT INTO {self.table_name}({name_string}) VALUES({value_string})"
        print(query)

        self.context.cursor.execute(query)

        self.context.connection.commit()

        model.id = int(self.context.cursor.lastrowid)
        self.data[model.id] = model

        self.onCreateOrUpdate(model)

        return model.id

    def remove(self, id):
        query = f"DELETE FROM {self.table_name} WHERE ID = \'{id}\'"
        print(query)
            
        self.context.cursor.execute(query)
        self.context.connection.commit()

        self.onDelete(self.data[id])

        self.data.pop(id)

    def get_all(self):
        return list(self.data.values())