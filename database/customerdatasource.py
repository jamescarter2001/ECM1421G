from .datasource import DataSource

from .model.contact import Contact
from .model.customer import Customer
from .model.contactxcustomer import ContactXCustomer

from .model.datafield import DataField
from .model.datarecord import DataRecord
from .model.fieldtype import FieldType

class CustomerDataSource(DataSource[ContactXCustomer]):
    def query(self):
        return "SELECT * FROM Contact INNER JOIN Customer on Contact.id = Customer.contactid"

    def add(self, model : ContactXCustomer):
        contact : Contact = model.contact
        customer : Customer = model.customer

        # Write Contact
        contact_record : DataRecord = DataRecord()

        if contact.id != 0:
            con_identity : DataField = DataField("id", contact.id, FieldType.number)
            contact_record.data.append(con_identity)

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
        
        contact_record.data.extend(list(filter(lambda f: f.data != "''", [firstname, lastname, street, town, postcode, county, phonelandline, phonemobile, phone3, email, what3words])))

        contact_name_string = contact_record.name_string()
        contact_value_string = contact_record.value_string()

        contact_query = f"INSERT INTO Contact({contact_name_string}) VALUES({contact_value_string})"
        print(contact_query)

        cursor = self.conn.cursor()
        cursor.execute(contact_query)
        self.conn.commit()

        contact_id = int(cursor.execute("SELECT @@IDENTITY").fetchone()[0])

        # Write Customer
        customer_record : DataRecord = DataRecord()

        if customer.id != 0:
            cus_identity : DataField = DataField("id", customer.id, FieldType.number)
            contact_record.data.append(cus_identity)

        contactid : DataField = DataField("contactid", contact_id, FieldType.number)
        addliinfo : DataField = DataField("addliinfo", customer.addliinfo)
        deliveryinfo : DataField = DataField("deliveryinfo", customer.deliveryinfo)
        
        customer_record.data.extend(list(filter(lambda f: f.data != "''", [contactid, addliinfo, deliveryinfo])))

        customer_name_string = customer_record.name_string()
        customer_value_string = customer_record.value_string()

        customer_query = f"INSERT INTO Customer({customer_name_string}) VALUES({customer_value_string})"
        print(customer_query)

        cursor.execute(customer_query)
        self.conn.commit()

        self.load()