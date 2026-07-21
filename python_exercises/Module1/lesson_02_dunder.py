"""
Lesson 1.2 - Dunder methods: __repr__, __str__, __eq__, __lt__

Fill in the TODOs. Run this file directly to test your work:
    python lesson_02_dunder.py
"""


class Book:
    total_books = 0

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
        Book.total_books += 1

    def checkout(self):
        if self.is_checked_out:
            return False
        self.is_checked_out = True
        return True

    def return_book(self):
        self.is_checked_out = False

    def __repr__(self):
        # TODO: return something like Book('Dune', 'Herbert', '123')
        return f"Book('{self.title}', '{self.author}', '{self.isbn}')"

    def __str__(self):
        # TODO: return something like "Dune by Herbert"
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        # TODO: if other is not a Book, return NotImplemented
        # TODO: otherwise compare by isbn
        if isinstance(other, Book):
            return self.isbn == other.isbn
        return NotImplemented

    def __lt__(self, other):
        # TODO: compare by title
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
    b1 = Book("Dune", "Herbert", "111")
    b2 = Book("Foundation", "Asimov", "222")
    b3 = Book("Neuromancer", "Gibson", "333")

    # TODO: print(b1) and print(repr(b1)) -- confirm they differ
    print(b1)
    print(repr(b1))

    # TODO: create b4 = Book(..., isbn="111") (same isbn as b1, different title/author is fine)
    # TODO: print(b1 == b4) -- should be True
    b4 = Book("b4", "sai", "111")
    print(b1 == b4)

    # TODO: sort [b1, b2, b3] with sorted() and print the titles in order
    sorted_books = sorted([b1,b2,b3])
    print([x.title for x in sorted_books])
