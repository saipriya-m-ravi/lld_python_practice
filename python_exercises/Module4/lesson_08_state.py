"""
Lesson 4.8 - State (final lesson)

Step 1: Implement Lost(BookState):
        - checkout(): print that a lost book can't be checked out, no transition
        - return_book(): print that it was found, THEN book.set_state(Available())
        - report_lost(): print that it's already marked lost, no transition
Step 2: Wire Book's three public methods to delegate to self._state.
Step 3: Walk the full lifecycle in __main__ and watch behavior change
        automatically as the state transitions -- no if/elif anywhere.
"""

from abc import ABC, abstractmethod


class BookState(ABC):
    @abstractmethod
    def checkout(self, book: "Book"):
        ...

    @abstractmethod
    def return_book(self, book: "Book"):
        ...

    @abstractmethod
    def report_lost(self, book: "Book"):
        ...


class Available(BookState):
    def checkout(self, book: "Book"):
        print(f"'{book.title}' checked out.")
        book.set_state(CheckedOut())

    def return_book(self, book: "Book"):
        print(f"'{book.title}' is already available -- nothing to return.")

    def report_lost(self, book: "Book"):
        print(f"'{book.title}' can't be lost -- it was never checked out.")


class CheckedOut(BookState):
    def checkout(self, book: "Book"):
        print(f"'{book.title}' is already checked out.")

    def return_book(self, book: "Book"):
        print(f"'{book.title}' returned.")
        book.set_state(Available())

    def report_lost(self, book: "Book"):
        print(f"'{book.title}' reported lost.")
        book.set_state(Lost())


# TODO: class Lost(BookState): -- see docstring at top for the three methods
class Lost(BookState):
    def checkout(self, book: "Book"):
        print(f"Lost book '{book.title}' cant be checked out.")

    def return_book(self, book: "Book"):
        print(f"'{book.title}' is found.")
        book.set_state(Available())

    def report_lost(self, book: "Book"):
        print(f"'{book.title}' is already reported lost.")

class Book:
    def __init__(self, title: str):
        self.title = title
        self._state: BookState = Available()

    def set_state(self, state: BookState):
        self._state = state

    # TODO: checkout(self) -> self._state.checkout(self)
    # TODO: return_book(self) -> self._state.return_book(self)
    # TODO: report_lost(self) -> self._state.report_lost(self)
    def checkout(self):
        return self._state.checkout(self)
    
    def return_book(self):
        return self._state.return_book(self)
    
    def report_lost(self):
        return self._state.report_lost(self)

if __name__ == "__main__":
    book = Book("Dune")

    book.checkout()        # Available -> CheckedOut
    book.checkout()        # already checked out -- no transition
    book.report_lost()     # CheckedOut -> Lost
    book.checkout()        # can't check out a lost book
    book.return_book()     # found! Lost -> Available
    book.checkout()        # Available -> CheckedOut again, proving the cycle works
