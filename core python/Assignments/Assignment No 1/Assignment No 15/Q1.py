class Book:
    def __init__(self, bid, pname, price, author):
        self.bid = bid
        self.pname = pname
        self.price = price
        self.author = author
    
    def getData(self):
        data = 'BOOK ID:'+str(self.bid)+'\n'
        data += 'BOOK NAME:'+self.pname+'\n'
        data += 'PRICE:'+str(self.price)+'\n'
        data += 'AUTHOR:'+self.author+'\n'
        return data

b1 = Book(101,'python basics', 500,'Guido')
b2 = Book(102,'C Programming', 300, 'Dennis Ritchie')

print(b1.getData())
print(b2.getData())