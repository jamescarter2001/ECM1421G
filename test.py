import pymssql

from database.model.contactxcustomer import ContactXCustomer
from database.model.operationresult import OperationResult
from database.model.connectiondata import ConnectionData
from database.model.contact import Contact
from database.model.customer import Customer

from db import DB

# Use the following data sources for each form:
# Customer List - db.contact_x_customer_source
# Add Customer - db.contact_x_customer_source
# Customer Orders - db.customer_x_orders_source
# Order Details - db.customer_x_orders_source

# Replace password before running script (See group chat).
cd : ConnectionData = ConnectionData("jamescarter2001.database.windows.net", "dts", "PASSWORD", "NymptonFoodHub")

try:
    # Initialise database connection and load into data sources, enclosed in try block to handle connection errors.
    db = DB(cd)

    # Use this to get all the data for the Customer Details page.
    customer_data = db.contact_x_customer_source.get_all()

    # Customer data is split between two database tables, "Contact" and "Customer". db.contact_x_customer_source joins them together.
    # The "Add Customer" form should construct these two objects from the user data, and then pass them to db.contact_x_customer_source.add()
    # No need to explicity provide the primary key "ID" field for either of these, on database write sucess, this is updated automatically in the data source.
    test_contact : Contact = Contact(firstname="hello", lastname="world")
    # No need to provide the contactid field for this class either, this is all handled by contact_x_customer_source when you pass it with contact data into db.contact_x_customer_source.add()
    test_customer : Customer = Customer(deliveryinfo="Test information")

    # Customer data manipulation returns the primary key ID given by the database for the new record.
    add_result : OperationResult = db.contact_x_customer_source.add(ContactXCustomer(test_contact, test_customer))

    # You can check if operation was successful.
    if add_result.success:
        added_data = db.contact_x_customer_source.get_for_id(add_result.id)
        db.contact_x_customer_source.remove(added_data)

    # Bad operations return a false status code and error message.
    bad_remove = db.contact_x_customer_source.remove(ContactXCustomer(contact=Contact(id=5000), customer=Customer(id=10000)))
    if bad_remove.success == False:
        print(bad_remove.error)

    # Customer orders can be loaded in using db.customer_x_orders.get_all(). This returns an array of orders, with customer (contact) data, as well as the order lines.
    customer_orders = db.customer_x_orders_source.get_all()

    print("Done.")
except pymssql.OperationalError as e:
    print(f"Connection Error: {e}")