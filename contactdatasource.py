from datasource import DataSource
from datarecord import DataRecord
from datafield import DataField

from model.contact import Contact

class ContactDataSource(DataSource[Contact]):
    def __init__(self, connection_data):
        super().__init__(connection_data=connection_data, table_name="Contact")

    def create_model(self, row):
        customer = Contact(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
        return customer

    def create_record(self, contact : Contact, new = False):
        record : DataRecord = DataRecord()

        if new == False:
            id : DataField = DataField("id", contact.id)
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

    def get_id(self, contact : Contact):
        return contact.id
    
    def get_for_id(self, id):
        for c in self.data:
            if c.id == id:
                return c