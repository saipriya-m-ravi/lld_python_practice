"""
Lesson 1.1 - Classes, __init__, instance vs class attributes

Fill in the TODOs. Run this file directly to test your work:
    python lesson_01_classes.py
"""


class Book:
    # TODO: add a class attribute `total_books` here, starting at 0
    total_books = 0

    def __init__(self, title, author, isbn):
        # TODO: set instance attributes: title, author, isbn, is_checked_out (default False)
        # TODO: increment Book.total_books
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
        Book.total_books += 1

    def checkout(self):
        # TODO: if already checked out, return False and do nothing else
        # TODO: otherwise set is_checked_out = True and return True
        if self.is_checked_out:
            return False
        self.is_checked_out = True
        return True

    def return_book(self):
        # TODO: set is_checked_out = False
        self.is_checked_out = False


class Library:
    def __init__(self):
        # TODO: set self.books = []
        self.books = []

    def add_book(self, book):
        # TODO: append book to self.books
        self.books.append(book)

    def find_by_isbn(self, isbn):
        # TODO: return the Book with matching isbn, or None if not found
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None


if __name__ == "__main__":
    # TODO: create 2-3 Book instances
    # TODO: create a Library, add the books
    # TODO: find one by isbn and check it out
    # TODO: try checking it out again -> should fail gracefully
    # TODO: print Book.total_books
    b1 = Book("title1", "author1", 1)
    b2 = Book("title2", "author2", 2)
    lib = Library()
    lib.add_book(b1)
    lib.add_book(b2)
    book = lib.find_by_isbn(2)
    print(book.checkout())
    print(book.checkout())
    print(Book.total_books)
    
    
