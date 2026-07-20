"""
Lesson 1.5 - Inheritance, super(), Abstract Base Classes

Fill in the TODOs. Run this file directly to test your work:
    python lesson_05_inheritance.py
"""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self._is_checked_out = False

    def checkout(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_item(self):
        self._is_checked_out = False

    @abstractmethod
    def late_fee_per_day(self):
        ...


class Book(LibraryItem):
    def __init__(self, title, isbn, author, price):
        # TODO: call super().__init__(title, isbn)
        # TODO: set self.author, self.price
        super().__init__(title, isbn)
        self.author = author
        self.price = price

    def late_fee_per_day(self):
        # TODO: return 0.50
        return 0.50


class DVD(LibraryItem):
    def __init__(self, title, isbn, runtime_minutes):
        # TODO: call super().__init__(title, isbn)
        # TODO: set self.runtime_minutes
        super().__init__(title, isbn)
        self.runtime_minutes = runtime_minutes

    def late_fee_per_day(self):
        # TODO: return 1.00
        return 1.00


if __name__ == "__main__":
    # TODO: try LibraryItem("x", "1") directly in a try/except -> expect TypeError, print it
    try:
        lib = LibraryItem("title", "1")
    except Exception as e:
        print(e)
    # TODO: create one Book and one DVD
    book = Book("title1", "1", "author1", 30)
    dvd = DVD("title2", "2", 200)
    # TODO: put both in a list, loop over it, print f"{item.title}: ${item.late_fee_per_day()}/day"
    #       for each -- do NOT use isinstance() or any type check in this loop
    libs = [book, dvd]
    for lib in libs:
        print(f"{lib.title}: ${lib.late_fee_per_day()}/day")
