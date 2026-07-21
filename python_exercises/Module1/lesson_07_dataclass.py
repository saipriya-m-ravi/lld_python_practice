"""
Lesson 1.7 - @dataclass

Fill in the TODOs. Run this file directly to test your work:
    python lesson_07_dataclass.py
"""

from dataclasses import dataclass, field


# Part A: auto __init__ / __repr__ / __eq__
@dataclass
class Member:
    # TODO: member_id: str
    # TODO: name: str
    # TODO: email: str
    # TODO: borrowed_books: list = field(default_factory=list)
    member_id: str
    name: str
    email: str
    borrowed_books: list = field(default_factory=list)


# Part C: frozen=True (immutable value object)
# TODO: decorate with @dataclass(frozen=True)
@dataclass(frozen=True)
class Money:
    # TODO: amount: float
    # TODO: currency: str
    amount: float
    currency: str


# Part D: order=True (auto comparison, field-by-field)
# TODO: decorate with @dataclass(order=True)
@dataclass(order=True)
class Version:
    # TODO: major: int
    # TODO: minor: int
    # TODO: patch: int
    major: int
    minor: int
    patch: int


if __name__ == "__main__":
    # --- Part A ---
    # TODO: m1 = Member("1", "Alice", "alice@x.com")
    # TODO: m2 = Member("1", "Alice", "alice@x.com")
    # TODO: print(m1)
    # TODO: print(m1 == m2)   -- should be True, different objects, same field values
    m1 = Member("1", "Alice", "alice@x.com")
    m2 = Member("1", "Alice", "alice@x.com")
    print(m1)
    print(m1==m2)
    
    # --- Part C ---
    # TODO: money = Money(50.0, "USD")
    # TODO: try money.amount = 100 in a try/except, print the caught exception
    money = Money(50.0, "USD")
    try:
        money.amount = 100
    except Exception as e:
        print(e)
    # --- Part D ---
    # TODO: create a few out-of-order Version(...) instances
    # TODO: sorted(...) them and print the results
    v1 = Version(1,2,3)
    v2 = Version(0,2,3)
    v3 = Version(1,2,3)
    v4 = Version(1,1,2)
    versions = [v1,v2,v3,v4]
    print(sorted(versions))
    
