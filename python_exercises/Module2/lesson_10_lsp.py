"""
Lesson 2.3 - Liskov Substitution Principle (LSP)

Step 1: Run this file as-is. Watch checkout_all() crash on ReferenceBook.
Step 2: Explain (to yourself) WHY this is an LSP violation -- not just
        "it crashed," but specifically: what promise did LibraryItem.checkout()
        make, and how did ReferenceBook.checkout() break that promise?
Step 3: Refactor so a ReferenceBook can exist in the system, alongside
        Book/DVD, WITHOUT checkout_all() needing any type-checks or
        try/except to special-case it.
"""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
    
    @abstractmethod
    def late_fee_per_day(self):
        pass


class CheckoutableItem(LibraryItem):
    def __init__(self, title, isbn):
        super().__init__(title, isbn)
        self._is_checked_out = False
    
    def checkout(self):
        """Contract: returns True if checkout succeeded, False if already
        checked out. Never raises for a normal checkout attempt."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_item(self):
        self._is_checked_out = False


class Book(CheckoutableItem):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def late_fee_per_day(self):
        return 0.50


class DVD(CheckoutableItem):
    def __init__(self, title, isbn, runtime_minutes):
        super().__init__(title, isbn)
        self.runtime_minutes = runtime_minutes

    def late_fee_per_day(self):
        return 1.00


class ReferenceBook(LibraryItem):
    """Reference books live in the library permanently -- they can never
    be checked out."""

    def __init__(self, title, isbn):
        super().__init__(title, isbn)

    def late_fee_per_day(self):
        return 0.0


def checkout_all(items: list[CheckoutableItem]):
    """Client code written against the LibraryItem contract: it expects
    checkout() to return True/False, nothing more."""
    for item in items:
        success = item.checkout()
        status = "checked out" if success else "already out"
        print(f"{item.title}: {status}")


if __name__ == "__main__":
    checkoutable_items = [
        Book("Dune", "111", "Herbert"),
        DVD("Interstellar", "222", 169)
    ]
    reference_items = [ReferenceBook("Encyclopedia Britannica", "333")]
    checkout_all(checkoutable_items)


# ============================================================
# TODO (after you've seen it crash and understand why):
#
# Refactor so that:
#   - Book and DVD can still be checked out exactly as before
#   - ReferenceBook can still exist as a LibraryItem (it has a title,
#     isbn, and late_fee_per_day -- those are legitimate)
#   - checkout_all() works over a mixed list WITHOUT crashing, and
#     WITHOUT adding any isinstance()/type check inside it
#
# Hint: the problem isn't that ReferenceBook exists -- it's that it's
# being forced to implement a capability (checkout) it fundamentally
# doesn't support. Consider splitting "checkout-ability" into its own
# interface, separate from LibraryItem, and only have checkout_all()
# operate on things that actually implement it.
# ============================================================
