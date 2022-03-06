from connectiondata import ConnectionData
from contactdatasource import ContactDataSource
from model.contact import Contact

cd : ConnectionData = ConnectionData("jamescarter2001.database.windows.net", "dts", "", "NymptonFoodHub")

contact_data_source = ContactDataSource(cd)
test : Contact = Contact(firstname="hello", lastname="world")
contact_data_source.add(test)

print("Done.")