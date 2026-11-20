#Abstraction

from abc import ABC, abstractmethod

class LibraryRules(ABC):
    @abstractmethod
    def return_book(self):
        pass
class ReturnBook(LibraryRules):
    def return_book(self):
        print("Book returned successfully")