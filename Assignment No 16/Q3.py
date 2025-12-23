class Shirt:
    size_increase ={
        "Small": 0,
        "Medium": 10,
        "Large": 20,
        "XLarge": 30
    }

    def __init__(self, sid=None, sname=None, type=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object destroyed")

    def showBook(self):
        final_price = self.getFinalPrice()
        print("ShIRT ID:", self.sid)
        print("SHIRT NAME:", self.sname)
        print("TYPE:", self.type)
        print("SIZE:", self.size)
        print("FINAL PRICE:", final_price)
        print()

    def getFinalPrice(self):
        increase = Shirt.size_increase.get(self.size, 0)
        return self.price + (self.price * increase / 100)

s1 = Shirt(1, "Puma", "Casual", 1000, "Small")
s2 = Shirt(2, "FabIndia", "Ethnic", 1000, "Medium")
s3 = Shirt(3, "Levis", "Formal", 1000, "Large")
s4 = Shirt(4, "Nike", "Sports", 1000, "XLarge")

s1.showBook()
s2.showBook()
s3.showBook()
s4.showBook()