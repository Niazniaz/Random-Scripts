class ITEMINFO:
    def __init__(self):
        self.ICode=0
        self.Item=""
        self.Price=0
        self.Qty=0
        self.Discount=0
        self.Netprice=0

    def buy(self):
        self.ICode=input("ENter item code")
        self.Item=raw_input("Enter item")
        self.Price=input("Enter price")
        self.Qty=input("Enter Qiuantity")
        self.findDisc()
    def findDisc(self):
        if self.Qty>=20:
            self.Discount=20
        elif self.Qty>=15:
            self.Discount=15
        elif self.Qty>=0:
            self.Discount=0

        self.Netprice=(self.Price*self.Qty)-self.Discount
    def showall(self):
        print self.ICode
        print self.Item
        print self.Price
        print self.Qty
        print self.Discount
        print self.Netprice

a=ITEMIFO()
a.buy()
a.showall()
        
