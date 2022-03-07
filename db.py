import pymssql

from database.contactdatasource import ContactDataSource
from database.customerxordersdatasource import CustomerXOrdersDataSource
from database.customerdatasource import CustomerDataSource
from database.contactxcustomerdatasource import ContactXCustomerDataSource
from database.model.connectioncontext import ConnectionContext
from database.orderxlinesdatasource import OrderXLinesDataSource
from database.salesorderdatasource import SalesOrderDataSource
from database.salesorderlinedatasource import SalesOrderLineDataSource

from database.model.connectiondata import ConnectionData

class DB:
    def __init__(self, connection_data : ConnectionData):
        db_connection = pymssql.connect(server=connection_data.server, user=connection_data.user, password=connection_data.password, database=connection_data.database)
        cursor = db_connection.cursor()

        connection_context = ConnectionContext(db_connection, cursor)

        # Table
        self.contact_source = ContactDataSource(connection_context)
        self.customer_source = CustomerDataSource(connection_context)
        self.sales_order_source = SalesOrderDataSource(connection_context)
        self.sales_order_line_source = SalesOrderLineDataSource(connection_context)

        # Join
        self.contact_x_customer_source = ContactXCustomerDataSource(self.contact_source, self.customer_source)
        self.order_x_lines_source = OrderXLinesDataSource(self.sales_order_source, self.sales_order_line_source)

        self.customer_x_orders_source = CustomerXOrdersDataSource(self.contact_source, self.order_x_lines_source)