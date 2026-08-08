"""
Lesson 4.7 - Observer

Step 1: Implement Book._notify_all() -- loop over self._observers,
        call .update(message) on each.
Step 2: Wire it into return_book() -- when a book is returned, everyone
        currently subscribed should be notified it's available again.
Step 3: Prove subscribe/unsubscribe are genuinely dynamic -- subscribe
        3 waitlisted members, unsubscribe ONE, then return the book and
        confirm only the remaining 2 get notified.
"""

from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        ...


class WaitlistMember(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"[{self.name}] notified: {message}")


class Book:
    def __init__(self, title: str, isbn: str):
        self.title = title
        self.isbn = isbn
        self._is_checked_out = False
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer):
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        self._observers.remove(observer)

    def checkout(self) -> bool:
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    # TODO: _notify_all(self, message: str)
    #   for each observer in self._observers: call observer.update(message)
    def _notify_all(self, message:str):
        for observer in self._observers:
            observer.update(message)

    # TODO: return_book(self)
    #   set self._is_checked_out = False
    #   call self._notify_all(f"'{self.title}' is now available!")
    def return_book(self):
        self._is_checked_out = False
        self._notify_all(f"'{self.title}' is now available!")

if __name__ == "__main__":
    book = Book("Dune", "111")
    book.checkout()   # someone already has it -- that's why others are waitlisting

    alice = WaitlistMember("Alice")
    bob = WaitlistMember("Bob")
    carol = WaitlistMember("Carol")

    # TODO: subscribe all three to `book`
    book.subscribe(alice)
    book.subscribe(bob)
    book.subscribe(carol)
    # TODO: unsubscribe bob specifically (he found a copy elsewhere)
    book.unsubscribe(bob)
    # TODO: call book.return_book() -- confirm only Alice and Carol are notified,
    #       NOT Bob
    book.return_book()
