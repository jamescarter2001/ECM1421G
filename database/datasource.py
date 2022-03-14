from typing import TypeVar, Generic

import pandas as pd

T = TypeVar('T')

class DataSource(Generic[T]):
    def query(self):
        raise NotImplementedError

    def add(self, T):
        raise NotImplementedError

    def __init__(self, conn):
        self.conn = conn
        self.load()

    def load(self):
        self.df = pd.read_sql(self.query(), self.conn)

    def get_all(self):
        return self.df