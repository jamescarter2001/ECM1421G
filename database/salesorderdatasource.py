from .datasource import DataSource
from .model.salesorder import SalesOrder

class SalesOrderDataSource(DataSource[SalesOrder]):
    def __init__(self, context):
        super().__init__(connection_context=context, table_name="SalesOrder")

    def create_model(self, row):
        sales_order = SalesOrder(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        return sales_order