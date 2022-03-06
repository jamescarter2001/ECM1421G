from datasource import DataSource
from datarecord import DataRecord
from datafield import DataField

from model.customer import Customer

class CustomerDataSource(DataSource[Customer]):
    def __init__(self, connection_data):
        super().__init__(connection_data=connection_data, table_name="Customer")

    def create_model(self, row):
        customer = Customer(row[0], row[1], row[2], row[3])
        return customer

    def create_record(self, customer : Customer, new = False):
        record : DataRecord = DataRecord()

        if new == False:
            id : DataField = DataField("id", customer.id)
            record.data.append(id)

        contactid : DataField = DataField("contactid", customer.id)
        addliinfo : DataField = DataField("addliinfo", customer.addliinfo)
        deliveryinfo : DataField = DataField("deliveryinfo", customer.deliveryinfo)
        
        record.data.extend(list(filter(lambda f: f.data != "''", [id, contactid, addliinfo, deliveryinfo])))

        return record

    def get_id(self, customer: Customer):
        return customer.id

    def get_for_id(self, id):
        for c in self.data:
            if c.id == id:
                return c