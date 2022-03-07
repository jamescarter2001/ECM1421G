from .model.orderxlines import OrderXLines

from .salesorderdatasource import SalesOrderDataSource
from .salesorderlinedatasource import SalesOrderLineDataSource

class OrderXLinesDataSource:
    def __init__(self, order_source, line_source):
        self.order_source : SalesOrderDataSource = order_source
        self.line_source : SalesOrderLineDataSource = line_source

        self.data : dict[int, OrderXLines] = {}
        self.load_data()

    def load_data(self):
        for order in list(self.order_source.data.values()):
            lines = list(filter(lambda l: l.orderid == order.id, list(self.line_source.data.values())))
            self.data[order.id] = OrderXLines(order, lines)