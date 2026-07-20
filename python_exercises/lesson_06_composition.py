"""
Lesson 1.6 - Composition vs Inheritance

Fill in the TODOs. Run this file directly to test your work:
    python lesson_06_composition.py
"""

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        ...


class EmailSender(NotificationSender):
    def send(self, message):
        # TODO: print(f"[EMAIL] {message}")
        pass


class SMSSender(NotificationSender):
    def send(self, message):
        # TODO: print(f"[SMS] {message}")
        pass


class Library:
    def __init__(self, notifier):
        # TODO: self.notifier = notifier
        # TODO: self.books = []
        pass

    def add_book(self, book):
        self.books.append(book)

    def notify_overdue(self, member, title):
        # TODO: build message f"{member}, '{title}' is overdue"
        # TODO: call self.notifier.send(message)
        pass


if __name__ == "__main__":
    # TODO: email_library = Library(EmailSender())
    # TODO: sms_library = Library(SMSSender())

    # TODO: email_library.notify_overdue("Alice", "Dune")
    # TODO: sms_library.notify_overdue("Bob", "Foundation")
    #       -- same Library.notify_overdue() code path, different output per injected notifier
    pass
