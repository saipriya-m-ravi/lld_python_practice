"""
Lesson 1.4 - @classmethod / @staticmethod

Fill in the TODOs. Run this file directly to test your work:
    python lesson_04_classmethod.py
"""


class Book:
    total_books = 0

    def __init__(self, title, author, isbn, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._is_checked_out = False
        self.price = price
        Book.total_books += 1

    def checkout(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        self._is_checked_out = False

    @property
    def is_checked_out(self):
        return self._is_checked_out

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Passed value is negative")
        self._price = value

    @staticmethod
    def is_valid_isbn(isbn):
        # TODO: return True if isbn is a non-empty string, else False
        return False if isbn == "" else True

    @classmethod
    def from_string(cls, data):
        # TODO: split `data` on "," into title, author, isbn, price
        # TODO: convert price to float
        # TODO: return cls(title, author, isbn, price)
        title, author, isbn, price = data.split(",")
        return cls(title, author, isbn, float(price))

    @classmethod
    def get_total_books(cls):
        # TODO: return cls.total_books
        return cls.total_books

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return NotImplemented

    def __lt__(self, other):
        return self.title < other.title


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None


if __name__ == "__main__":
    # TODO: print(Book.is_valid_isbn("111")) and print(Book.is_valid_isbn(""))
    #       -- call these WITHOUT creating any Book instance first
    print(Book.is_valid_isbn("111")) 
    print(Book.is_valid_isbn("")) 
    # TODO: b1 = Book.from_string("Dune,Herbert,111,20") -- print(b1)
    b1 = Book.from_string("Dune,Herbert,111,20")
    print(b1)
    # TODO: print(Book.get_total_books())
    print(Book.get_total_books())
