from .datasource import DataSource

class OrderDataSource(DataSource):
    def query(self):
        return "SELECT * FROM SalesOrder"

    def get_for_customer(self, id):
        return self.df.loc[self.df['customerid'] == id]