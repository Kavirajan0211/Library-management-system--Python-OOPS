📚 Library Management System Using Python OOP
📌 Project Description

The Library Management System is a simple Python project developed using Object-Oriented Programming (OOP) concepts.

This project demonstrates the five major OOP concepts:

Classes and Objects
Encapsulation
Inheritance
Polymorphism
Abstraction

The system allows users to add books, display available books, borrow books, and view the total number of books.

🎯 Project Objectives
To understand Python Object-Oriented Programming.
To implement the five major OOP concepts.
To organize Python code into multiple files.
To understand how Python modules and imports work.
To build a simple Library Management System.
📁 Project Structure
text
Library-Management-System/
│
├── book.py
├── library.py
├── user.py
├── rules.py
├── main.py
└── README.md

File Description
File	Purpose
book.py	Classes and Objects
library.py	Encapsulation
user.py	Inheritance and Polymorphism
rules.py	Abstraction
main.py	Connects all Python files
1. Classes and Objects – book.py
Code
python
class Book:
    def __init__(self,title,quantity):
        self.title=title
        self.quantity=quantity

Explanation

1. class Book:

Defines a class named Book.
A class is a blueprint used to create objects.

2. def __init__(self,title,quantity):

This is a constructor.
It is automatically called when an object is created.
It initializes the book details.

3. self.title=title

Stores the book title inside the object.
self refers to the current object.

4. self.quantity=quantity

Stores the available quantity of the book.
Object Creation
python
Book("Python",5)
Book("Java",7)

These statements create two Book objects.
The first object represents Python with quantity 5.
The second object represents Java with quantity 7.
OOP Concept Used

Classes and Objects: The Book class acts as a blueprint, and individual books are created as objects.

2. Encapsulation – library.py
Code
python
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

Explanation

1. from book import Book

Imports the Book class from book.py.
Allows us to use the Book class in this file.

2. class Library:

Creates a class named Library.
This class manages the books in the library.

3. self.books=[]

Creates an empty list.
Stores all the book objects.

4. self.__total=0

Creates a private variable.
Double underscore (__) indicates name mangling in Python.
It helps restrict direct access to the variable.

5. def add_book(self,book):

Accepts a book object as an argument.
Adds the book object to the library list.

6. self.books.append(book)

Adds the book to the list.

7. self.__total+=1

Increases the total book entries by one.

8. def borrow(self,title):

Accepts the title of the book to be borrowed.

9. for book in self.books:

Iterates through all the books in the library.

10. if book.title==title and book.quantity > 0:

Checks whether the requested book exists.
Checks whether the book quantity is greater than zero.

11. book.quantity-=1

Decreases the available quantity by one.

12. return

Stops the method after successfully borrowing the book.

13. print("Book not available")

Displays a message if the requested book is unavailable.

14. def display(self):

Displays all the books and their quantities.

15. def total_books(self):

Returns the total number of book entries.
Provides controlled access to the private __total variable.
OOP Concept Used

Encapsulation: The __total variable is private, and the total_books() method provides controlled access to it.

3. Inheritance and Polymorphism – user.py
Code
python
class User:
    def __init__(self,name):
        self.name=name

class Student(User):
    def borrow(self):
        print(self.name, "is a student borrowing a book")

class Teacher(User):
    def borrow(self):
        print(self.name, "is a teacher borrowing a book")

Explanation

1. class User:

Creates a parent class named User.
Contains common properties shared by students and teachers.

2. def __init__(self,name):

Constructor initializes the user's name.

3. self.name=name

Stores the user's name.

4. class Student(User):

Creates a Student class.
Inherits properties and methods from the User class.
User is the parent class, and Student is the child class.

5. class Teacher(User):

Creates a Teacher class.
Also inherits from the User class.

6. def borrow(self):

Defines a borrowing method inside the Student and Teacher classes.
Both classes have the same method name but their own implementations.
Object Creation
python
student=Student("Arun")
teacher=Teacher("Malathy")

Creates a Student object with the name Arun.
Creates a Teacher object with the name Malathy.
OOP Concepts Used

Inheritance: Student and Teacher inherit the common properties of the User class.

Polymorphism: Both Student and Teacher have a method named borrow(), but each provides a different message.

4. Abstraction – rules.py
Code
python
from abc import ABC, abstractmethod

class LibraryRules(ABC):

    @abstractmethod
    def return_book(self):
        pass

class ReturnBook(LibraryRules):

    def return_book(self):
        print("Book returned successfully")

Explanation

1. from abc import ABC, abstractmethod

Imports ABC and abstractmethod.
These are used to implement abstraction in Python.

2. class LibraryRules(ABC):

Creates an abstract class named LibraryRules.
ABC stands for Abstract Base Class.

3. @abstractmethod

Defines a method that must be implemented by a concrete child class.

4. def return_book(self):

Declares an abstract method.
It does not contain the actual implementation.

5. pass

Represents an empty method body.
The actual functionality is implemented in the child class.

6. class ReturnBook(LibraryRules):

Creates a child class that inherits LibraryRules.

7. def return_book(self):

Implements the abstract method.

8. print("Book returned successfully")

Displays the return confirmation message.
Object Creation
python
return_book=ReturnBook()
return_book.return_book()

Creates an object of ReturnBook.
Calls the implemented return_book() method.
OOP Concept Used

Abstraction: The abstract class defines what operation must be implemented, while the child class provides the implementation.

5. Main Program – main.py
Code
python
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

Explanation

1. Import Statements

python
from book import Book
from library import Library
from user import Student,Teacher
from rules import ReturnBook

Imports all required classes from the other Python files.
Connects all the modules into one program.

2. Library Object Creation

python
library=Library()

Creates an object of the Library class.
Initializes an empty book list.

3. Adding Books

python
library.add_book(Book("Python",5))
library.add_book(Book("Java",7))

Creates two Book objects.
Adds both books to the library.
Python has quantity 5.
Java has quantity 7.

4. Creating User Objects

python
student=Student("Arun")
teacher=Teacher("Malathy")

Creates a Student object.
Creates a Teacher object.

5. Displaying Books

python
library.display()

Displays all available books and their quantities.

6. Borrowing Books

python
student.borrow()
library.borrow("Python")

Calls the Student borrowing method.
Borrows the Python book.
Decreases the quantity from 5 to 4.
python
teacher.borrow()
library.borrow("Java")

Calls the Teacher borrowing method.
Borrows the Java book.
Decreases the quantity from 7 to 6.

7. Returning a Book

python
return_book=ReturnBook()
return_book.return_book()

Creates an object of ReturnBook.
Calls the abstraction implementation.

8. Displaying Total Books

python
print("Total books: ",library.total_books())

Calls the total_books() method.
Displays the total number of book entries.
▶️ How to Run the Project
Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Step 2: Create a Project Folder

Create a folder named Library-Management-System.

Step 3: Create Python Files

Create these five files:

book.py
library.py
user.py
rules.py
main.py
Step 4: Run the Main File

Open the terminal inside your project folder and execute:

bash
python main.py

💻 Expected Output
text
Book added successfully
Book added successfully

Python 5
Java 7

Arun is a student borrowing a book
Book borrowed successfully

Malathy is a teacher borrowing a book
Book borrowed successfully

Book returned successfully

Total books: 2

📚 OOP Concepts Summary
OOP Concept	Implementation	File
Classes and Objects	Book class and its objects	book.py
Encapsulation	Private __total variable	library.py
Inheritance	Student and Teacher inherit User	user.py
Polymorphism	Same borrow() method in different classes	user.py
Abstraction	ABC and abstractmethod	rules.py
🚀 Conclusion

This Library Management System is a beginner-level Python project that demonstrates all five major Object-Oriented Programming concepts.

By developing this project, I learned how to:

Create classes and objects.
Protect data using encapsulation.
Reuse code using inheritance.
Implement polymorphism through method overriding.
Achieve abstraction using abstract classes.
Organize and connect multiple Python files using imports.

This project helped me understand how Object-Oriented Programming concepts work together in a real-world application.
