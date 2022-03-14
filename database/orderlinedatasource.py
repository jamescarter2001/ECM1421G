from .datasource import DataSource

class OrderLineDataSource(DataSource):
    def query(self):
        return "SELECT * FROM SalesOrderLine"

    def get_for_order(self, id):
        return self.df.loc[self.df['orderid'] == id]