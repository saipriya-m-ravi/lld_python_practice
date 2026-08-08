"""
Lesson 4.5 - Facade

Step 1: Study checkout_book() -- notice it's the ONLY place that knows
        the right order to call across all four subsystems.
Step 2: Implement return_book() the same way:
        - mark_returned in InventorySystem
        - if days_late > 0: calculate a fee (flat $0.50/day is fine),
          charge it via BillingSystem, and notify the member
        - return True
"""


# ------------------------------------------------------------------
# Subsystems -- individually simple, but there are FOUR of them, and
# using the library correctly means coordinating all four in order.
# ------------------------------------------------------------------

class InventorySystem:
    def __init__(self):
        self._checked_out: set[str] = set()

    def check_availability(self, isbn: str) -> bool:
        return isbn not in self._checked_out

    def mark_checked_out(self, isbn: str):
        self._checked_out.add(isbn)

    def mark_returned(self, isbn: str):
        self._checked_out.discard(isbn)


class MemberSystem:
    def __init__(self):
        self._members = {
            "m1": {"active": True, "email": "alice@example.com"},
            "m2": {"active": False, "email": "bob@example.com"},
        }

    def is_member_active(self, member_id: str) -> bool:
        return self._members.get(member_id, {}).get("active", False)

    def get_member_email(self, member_id: str) -> str:
        return self._members[member_id]["email"]


class NotificationSystem:
    def send(self, email: str, message: str):
        print(f"[EMAIL to {email}] {message}")


class BillingSystem:
    def charge_late_fee(self, member_id: str, amount: float):
        print(f"[BILLING] charged member {member_id} ${amount:.2f}")


# ------------------------------------------------------------------
# WORKED EXAMPLE -- the facade
# ------------------------------------------------------------------

class LibraryFacade:
    def __init__(self):
        self.inventory = InventorySystem()
        self.members = MemberSystem()
        self.notifications = NotificationSystem()
        self.billing = BillingSystem()

    def checkout_book(self, member_id: str, isbn: str) -> bool:
        if not self.members.is_member_active(member_id):
            print(f"Checkout denied: member {member_id} is not active")
            return False
        if not self.inventory.check_availability(isbn):
            print(f"Checkout denied: book {isbn} is not available")
            return False

        self.inventory.mark_checked_out(isbn)
        email = self.members.get_member_email(member_id)
        self.notifications.send(email, f"You checked out '{isbn}'")
        return True

    # TODO: return_book(self, member_id: str, isbn: str, days_late: int = 0) -> bool
    #   - self.inventory.mark_returned(isbn)
    #   - if days_late > 0:
    #       fee = days_late * 0.50
    #       self.billing.charge_late_fee(member_id, fee)
    #       email = self.members.get_member_email(member_id)
    #       self.notifications.send(email, f"Late fee charged: ${fee:.2f}")
    #   - return True
    def return_book(self, member_id: str, isbn: str, days_late: int = 0) -> bool:
        self.inventory.mark_returned(isbn)
        if days_late > 0:
            fee = days_late * 0.50
            self.billing.charge_late_fee(member_id, fee)
            email = self.members.get_member_email(member_id)
            self.notifications.send(email, f"Late fee charged: ${fee:.2f}")
        return True

            
if __name__ == "__main__":
    library = LibraryFacade()

    # active member, available book -- should succeed
    print(library.checkout_book("m1", "111"))

    # inactive member -- should be denied
    print(library.checkout_book("m2", "222"))

    # already checked out -- should be denied
    print(library.checkout_book("m1", "111"))

    print(library.return_book("m1", "111", days_late=0))
    print(library.checkout_book("m1", "111"))
    print(library.return_book("m1", "111", days_late=3))
    # TODO: library.return_book("m1", "111", days_late=0) -- no fee
    # TODO: library.checkout_book("m1", "111") again, then
    #       library.return_book("m1", "111", days_late=3) -- should charge $1.50
