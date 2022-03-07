class SalesOrder:
    def __init__(self, id, customerid, orderdate, picked, delivered, invoiced, paid, complete, goodscost, extrasinfo, extrascost, deliverycost, totalcost):
        self.id = id
        self.customerid = customerid
        self.orderdate = orderdate
        self.picked = picked
        self.delivered = delivered
        self.invoiced = invoiced
        self.paid = paid
        self.complete = complete
        self.goodscost = goodscost
        self.extrasinfo = extrasinfo
        self.extrascost = extrascost
        self.deliverycost = deliverycost
        self.totalcost = totalcost