"""
Lesson 1.3 - Encapsulation with @property

Fill in the TODOs. Run this file directly to test your work:
    python lesson_03_property.py
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

    # TODO: add a read-only property `is_checked_out` (getter only, no setter)
    #       that returns self._is_checked_out
    @property
    def is_checked_out(self):
        return self._is_checked_out

    # TODO: add a `price` property:
    #   - getter returns self._price
    #   - setter raises ValueError if value < 0, otherwise sets self._price = value
    @property
    def price(self):
        return self._price
   
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Passed value is negative")
        self._price = value

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
    b1 = Book("Dune", "Herbert", "111", 20)

    # TODO: try b1.is_checked_out = True directly -- expect AttributeError, catch and print it
    try:
        b1.is_checked_out = True
    except Exception as e:
        print(e)
        
    # TODO: try b1.price = -5 -- expect ValueError, catch and print it
    try:
        b1.price = -5
    except Exception as e:
        print(e)
 
    # TODO: set b1.price = 15 (valid), then print(b1.price)
    try:
        b1.price = 15
    except Exception as e:
        print(e)
    print(b1.price)