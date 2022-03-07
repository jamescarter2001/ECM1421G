class SalesOrderLine:
    def __init__(self, id, orderid, stockitemid, itemqty, itemname, itemunit, itemprice, itemcost):
        self.id = id
        self.orderid = orderid
        self.stockitemid = stockitemid
        self.itemqty = itemqty
        self.itemname = itemname
        self.itemunit = itemunit
        self.itemprice = itemprice
        self.itemcost = itemcost