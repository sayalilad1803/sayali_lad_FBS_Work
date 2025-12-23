class Product:
    discount = 10 

    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print("Product object destroyed")

    def showBook(self):
        print("Product ID :", self.pid)
        print("Product Name :", self.pname)
        print("Price :", self.price)
        print("Quantity :", self.quantity)

    def applyDiscount(self):
        discount_amt = (self.price * Product.discount) / 100
        return self.price - discount_amt

p1 = Product(1, "Laptop", 50000, 2)
p2 = Product(2, "Mobile", 20000, 1)

p1.showBook()
print("Price after discount:", p1.applyDiscount())
print()

p2.showBook()
print("Price after discount:", p2.applyDiscount())