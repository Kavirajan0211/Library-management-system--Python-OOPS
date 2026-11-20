#Encapsulation

from book import Book
class Library:
    def __init__(self):
        self.books=[]
        self.__total=0
    def add_book(self,book):
        self.books.append(book)
        self.__total+=1
        print("Book added successfully")
    def borrow(self,title):
        for book in self.books:
            if book.title==title and book.quantity > 0:
                book.quantity-=1
                print("Book borrowed successfully")
                return
        print("Book not available")
    def display(self):
        for book in self.books:
            print(book.title,book.quantity)
    def total_books(self):
        return self.__total