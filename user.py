#Inheritance and Polymorphism

class User:
    def __init__(self,name):
        self.name=name
class Student(User):
    def borrow(self):
        print(self.name, "is a student borrowing a book")
class Teacher(User):
    def borrow(self):
        print(self.name, "is a teacher borrowing a book")