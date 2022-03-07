from sqlite3 import OperationalError

from .model.contactxcustomer import ContactXCustomer
from .model.operationresult import OperationResult

from .contactdatasource import ContactDataSource
from .customerdatasource import CustomerDataSource

class ContactXCustomerDataSource:
    def __init__(self, contact_source, customer_source):
        self.contact_source : ContactDataSource = contact_source
        self.customer_source : CustomerDataSource = customer_source
        self.data : dict[int, ContactXCustomer] = {}

        self.load_data()
    
    def load_data(self):
        for contact in list(self.contact_source.data.values()):
            for customer in list(self.customer_source.data.values()):
                if contact.id == customer.contactid:
                    contact_customer : ContactXCustomer = ContactXCustomer(contact, customer)
                    self.data[contact.id] = contact_customer

    def add(self, contact_customer : ContactXCustomer):
        try:
            contactid = self.contact_source.add(contact_customer.contact)

            contact_customer.customer.contactid = contactid
            self.customer_source.add(contact_customer.customer)

            self.data[contact_customer.contact.id] = contact_customer

            return OperationResult(id=contact_customer.contact.id)
        except OperationalError as e:
            return OperationResult(success=False, error=e)

    def remove(self, contact_customer : ContactXCustomer):
        try:
            self.customer_source.remove(contact_customer.customer.id)
            self.contact_source.remove(contact_customer.contact.id)

            self.data.pop(contact_customer.contact.id)

            return OperationResult(id=contact_customer.contact.id)

        except OperationalError as e:
            return OperationResult(success=False, error=f"Operational error: {e}")
        except KeyError as e:
            return OperationResult(success=False, error=f"Invalid key: {e}")

    def get_for_id(self, id):
        return self.data[id]

    def get_all(self):
        return list(self.data.values())