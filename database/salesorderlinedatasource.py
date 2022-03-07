from .datasource import DataSource
from .model.salesorderline import SalesOrderLine

class SalesOrderLineDataSource(DataSource[SalesOrderLine]):
    def __init__(self, context):
        super().__init__(connection_context=context, table_name="SalesOrderLine")

    def create_model(self, row):
        sales_order_line = SalesOrderLine(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
        return sales_order_line