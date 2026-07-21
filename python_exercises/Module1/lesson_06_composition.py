"""
Lesson 1.6 - Composition vs Inheritance

Fill in the TODOs. Run this file directly to test your work:
    python lesson_06_composition.py
"""

from abc import ABC, abstractmethod


class NotificationSender(ABC):
    @abstractmethod
    def send(self, message):
        """Send due notifications via notifier"""


class EmailSender(NotificationSender):
    def send(self, message):
        # TODO: print(f"[EMAIL] {message}")
        print(f"[Email] {message}")


class SMSSender(NotificationSender):
    def send(self, message):
        # TODO: print(f"[SMS] {message}")
        print(f"[SMS] {message}")


class Library:
    def __init__(self, notifier):
        self.notifier = notifier
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def notify_overdue(self, member, title):
        # TODO: build message f"{member}, '{title}' is overdue"
        # TODO: call self.notifier.send(message)
        message = f"{member}, '{title}' is overdue"
        self.notifier.send(message)


if __name__ == "__main__":
    email_library = Library(EmailSender())
    sms_library = Library(SMSSender())

    email_library.notify_overdue("Alice", "Dune")
    sms_library.notify_overdue("Bob", "Foundation")
    
