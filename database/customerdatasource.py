from .datasource import DataSource
from .model.datarecord import DataRecord
from .model.datafield import DataField
from .model.fieldtype import FieldType

from .model.customer import Customer

class CustomerDataSource(DataSource[Customer]):
    def __init__(self, context):
        super().__init__(connection_context=context, table_name="Customer")

    def create_model(self, row):
        customer = Customer(row[0], row[1], row[2], row[3])
        return customer

    def create_record(self, customer : Customer, new = False):
        record : DataRecord = DataRecord()

        if new == False:
            id : DataField = DataField("id", customer.id, FieldType.number)
            record.data.append(id)

        contactid : DataField = DataField("contactid", customer.contactid, FieldType.number)
        addliinfo : DataField = DataField("addliinfo", customer.addliinfo)
        deliveryinfo : DataField = DataField("deliveryinfo", customer.deliveryinfo)
        
        record.data.extend(list(filter(lambda f: f.data != "''", [contactid, addliinfo, deliveryinfo])))

        return record