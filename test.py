from database.model.contact import Contact
from database.model.customer import Customer
from database.model.contactxcustomer import ContactXCustomer

from db import DB
from database.model.connectiondata import ConnectionData

cd : ConnectionData = ConnectionData("jamescarter2001.database.windows.net", "dts", "PASS", "NymptonFoodHub")

# DB interaction object, wrap instantiation in try-catch on login page, looping until successful connection.
db : DB = DB(cd)

# use the following data sources in views.

# db.customer_source - customers
# db.order_source - orders
# db.order_line_source - order details

# Populate with user entered data.
test_contact : Contact = Contact(firstname="hello", lastname="world")
test_customer : Customer = Customer(deliveryinfo="Test information")

# Save customer data to database.
db.customer_source.add(ContactXCustomer(test_contact, test_customer))

# Pass in customer id.
customer_orders = db.order_source.get_for_customer(3)

# Pass in order id.
order_lines = db.order_line_source.get_for_order(1)