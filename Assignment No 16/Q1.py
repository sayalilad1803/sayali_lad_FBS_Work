class Book:
    count = 0  

    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1

    def __del__(self):
        print("Book object destroyed")

    def showBook(self):
        print("Book ID :", self.bid)
        print("Book Name :", self.bname)
        print("Price :", self.price)
        print("Author :", self.author)
        print()

b1 = Book(101, "Let Us C", 450, "Denis Ritchie")
b2 = Book(102, "Mastering SQL", 250, "Loni")
b3 = Book()

b1.showBook()
b2.showBook()
b3.showBook()

print("Total Book objects:", Book.count)

