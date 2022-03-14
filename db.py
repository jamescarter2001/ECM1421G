import pyodbc

from database.model.connectiondata import ConnectionData

from database.customerdatasource import CustomerDataSource
from database.orderdatasource import OrderDataSource
from database.orderlinedatasource import OrderLineDataSource
class DB:
    def __init__(self, connection_data : ConnectionData):
        conn = pyodbc.connect(f'Driver=SQL Server;Server={connection_data.server};Database={connection_data.database};UID={connection_data.user};PWD={connection_data.password}')

        self.customer_source : CustomerDataSource = CustomerDataSource(conn)
        self.order_source : OrderDataSource = OrderDataSource(conn)
        self.order_line_source : OrderLineDataSource = OrderLineDataSource(conn)