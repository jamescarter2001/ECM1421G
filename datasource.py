from typing import TypeVar, Generic

from sqlite3 import Cursor
import pymssql

from connectiondata import ConnectionData
from datarecord import DataRecord

T = TypeVar('T')

class DataSource(Generic[T]):
    def __init__(self, connection_data : ConnectionData, table_name):
        self.connection_data = connection_data
        self.table_name = table_name
        
        self.data : dict[int, T] = {}

        self.load_data()

    def connect(self):
        conn = pymssql.connect(server=self.connection_data.server, user=self.connection_data.user, password=self.connection_data.password, database=self.connection_data.database)
        cursor = conn.cursor()

        self.__conn = conn
        self.__cursor : Cursor = cursor

    def create_model(self, row) -> T:
        raise NotImplementedError

    def create_record(self, model : T) -> DataRecord:
        raise NotImplementedError

    def get_for_id(self, id):
        raise NotImplementedError

    def load_data(self):
        self.connect()

        self.__cursor.execute(f"SELECT * FROM {self.table_name}")
        row = self.__cursor.fetchone()

        while row:
            model : T = self.create_model(row)
            self.data[model.id] = model
            row = self.__cursor.fetchone()

    def add(self, model : T):

        if model.id == 0:
            r : DataRecord = self.create_record(model, new=True)
        else:
            r : DataRecord = self.create_record(model)

        name_string = ', '.join(list(map(lambda x: x.name, r.data)))
        value_string = ', '.join(list(map(lambda x: x.data, r.data)))

        query = f"INSERT INTO {self.table_name}({name_string}) VALUES({value_string})"
        print(query)

        self.__cursor.execute(query)

        self.__conn.commit()
        self.data[model.id] = model

    def remove(self, id):
        self.__cursor.execute(f"DELETE FROM {self.table_name} WHERE ID = \'{id}\'")
        self.__conn.commit()

        self.data.pop(id)

    def get_all(self):
        return self.data