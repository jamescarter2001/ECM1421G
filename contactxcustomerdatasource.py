from contactxcustomer import ContactXCustomer

from contactdatasource import ContactDataSource
from customerdatasource import CustomerDataSource

class ContactXCustomerDataSource:
    def __init__(self, contact_source, customer_source):
        self.contact_source : ContactDataSource = contact_source
        self.customer_source : CustomerDataSource = customer_source

        self.data : dict[int, ContactXCustomer] = []
    
    def load_data(self):
        for contact in self.contact_source.data:
            for customer in self.customer_source.data:
                if contact.id == customer.contactid:
                    contact_customer : ContactXCustomer = ContactXCustomer(contact, customer)
                    self.data[contact.id] = contact_customer

    def update(self, contact_customer : ContactXCustomer):
        self.contact_source.add(contact_customer.contact)
        self.customer_source.add(contact_customer.customer)
        
        self.data[contact_customer.contact.id] = contact_customer

    def get_all(self):
        return self.data