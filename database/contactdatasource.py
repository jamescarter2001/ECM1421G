from .model.datarecord import DataRecord
from .model.datafield import DataField
from .model.fieldtype import FieldType
from .model.contact import Contact

from .datasource import DataSource

class ContactDataSource(DataSource[Contact]):
    def __init__(self, context):
        super().__init__(connection_context=context, table_name="Contact")

    def create_model(self, row):
        customer = Contact(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        return customer

    def create_record(self, contact : Contact, new = False):
        record : DataRecord = DataRecord()

        if new == False:
            id : DataField = DataField("id", contact.id, FieldType.number)
            record.data.append(id)
        
        firstname : DataField = DataField("firstname", contact.firstname)
        lastname : DataField = DataField("lastname", contact.lastname)
        street : DataField = DataField("street", contact.street)
        town : DataField = DataField("town", contact.town)
        postcode : DataField = DataField("postcode", contact.postcode)
        county : DataField = DataField("county", contact.county)
        phonelandline : DataField = DataField("phonelandline", contact.phonelandline)
        phonemobile : DataField = DataField("phonemobile", contact.phonemobile)
        phone3 : DataField = DataField("phone3", contact.phone3)
        email : DataField = DataField("email", contact.email)
        what3words : DataField = DataField("what3words", contact.what3words)
        
        record.data.extend(list(filter(lambda f: f.data != "''", [firstname, lastname, street, town, postcode, county, phonelandline, phonemobile, phone3, email, what3words])))

        return record