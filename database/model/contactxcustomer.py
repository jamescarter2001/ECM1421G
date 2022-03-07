from .contact import Contact
from .customer import Customer

class ContactXCustomer:
    def __init__(self, contact, customer):
        self.contact : Contact = contact
        self.customer : Customer = customer