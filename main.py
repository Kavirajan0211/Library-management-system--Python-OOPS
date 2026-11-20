#Connecting all the files

from book import Book
from library import Library
from user import Student,Teacher
from rules import ReturnBook

library=Library()

library.add_book(Book("Python",5))
library.add_book(Book("Java",7))

student=Student("Arun")
teacher=Teacher("Malathy")

library.display()

student.borrow()
library.borrow("Python")

teacher.borrow()
library.borrow("Java")

return_book=ReturnBook()
return_book.return_book()
print("Total books: ",library.total_books())