"""
Lesson 2.1 - Single Responsibility Principle (SRP)

Step 1: Read BadMember below. Do not change it yet.
Step 2: List (as comments, or just think it through) every distinct
        "reason this class would need to change." Aim for at least 3.
Step 3: Scroll down to the TODO section and refactor into multiple
        classes, each with exactly one responsibility, while preserving
        the same overall behavior when run.
"""

import datetime
from dataclasses import dataclass, field


class BadMember:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.borrowed_books = {}  # isbn -> due_date

    def borrow_book(self, isbn, days_allowed=14):
        due_date = datetime.date.today() + datetime.timedelta(days=days_allowed)
        self.borrowed_books[isbn] = due_date

    def calculate_late_fee(self, isbn):
        due_date = self.borrowed_books[isbn]
        days_late = (datetime.date.today() - due_date).days
        if days_late <= 0:
            return 0.0
        return days_late * 0.50

    def send_overdue_email(self, isbn):
        fee = self.calculate_late_fee(isbn)
        if fee > 0:
            print(f"Sending email to {self.email}: '{isbn}' is overdue, fee: ${fee}")

    def save_to_database(self):
        # pretend this hits a real DB
        print(f"INSERT INTO members VALUES ({self.member_id}, '{self.name}', '{self.email}')")


# ============================================================
# TODO: Refactor.
#
# Split BadMember's responsibilities into separate classes.
# Think about: what changes independently from what?
#   - The shape of a member's data
#   - The rule for how late fees are calculated
#   - How overdue notices are delivered
#   - How a member gets persisted
#
# Keep Member's own data/behavior about being a member, and move
# everything else out into collaborator classes that Member's
# calling code coordinates between (not necessarily Member itself).
# ============================================================
from abc import ABC, abstractmethod
class NotificationSender(ABC):  
    @abstractmethod
    def send_message(self):
        pass

class Email(NotificationSender):
    def send_message(self, email, isbn, fee):
        print(f"Sending email to {email}: '{isbn}' is overdue, fee: ${fee}")

@dataclass
class Member:
    member_id: int
    name: str
    email: str
    notifier: NotificationSender
    borrowed_books: dict = field(default_factory=dict)
    
    def borrow_book(self, isbn, due_date):
        self.borrowed_books[isbn] = due_date


class MemberRepository:
    def save(self, member):
        # pretend this hits a real DB
        print(f"INSERT INTO members VALUES ({member.member_id}, '{member.name}', '{member.email}')")


def late_fee_calculator(due_date):
    days_late = (datetime.date.today() - due_date).days
    if days_late <= 0:
        return 0.0
    return days_late * 0.50

    
if __name__ == "__main__":
    m1 = Member(1, "sai", "sai.g.com", Email(), {})
    past_date = datetime.date.today() - datetime.timedelta(days=5)
    m1.borrow_book(123, past_date)
    
    fee = late_fee_calculator(m1.borrowed_books[123])
    if fee > 0:
        m1.notifier.send_message(m1.email, 123, fee)
    
    repo = MemberRepository()
    repo.save(m1)
    

    # TODO: rebuild the same end-to-end flow using your refactored classes:
    #   1. create a member
    #   2. borrow a book with a due_date already in the past (so it's late)
    #      -- hint: you can directly set the returned due date backwards for testing,
    #         or add a days_allowed=-5 to simulate an already-overdue book
    #   3. calculate its late fee
    #   4. send the overdue notice
    #   5. "save" the member
    # every step should still work, just via separate, focused classes
