from .model.contactxorder import ContactXOrder

class CustomerXOrdersDataSource:
    def __init__(self, contact_source, sales_x_lines_source):
        self.contact_source = contact_source
        self.sales_x_lines_source = sales_x_lines_source

        self.data : dict[int, ContactXOrder] = {}
        self.load_data()

    def load_data(self):
        for contact in list(self.contact_source.data.values()):
            orders = list(filter(lambda l: l.sales_order.customerid == contact.id, list(self.sales_x_lines_source.data.values())))
            for order in orders:
                self.data[order.sales_order.id] = ContactXOrder(contact, order)
    
    def get_all(self):
        return list(self.data.values())