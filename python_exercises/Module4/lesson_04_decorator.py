"""
Lesson 4.4 - Decorator (design pattern)

Step 1: Implement GiftWrapDecorator (+$5 flat), ExpressShippingDecorator
        (+$10 flat), InsuranceDecorator (+2% of whatever price it receives
        from the object it wraps).
Step 2: Stack all three around a Book in one order, print the price.
Step 3: Stack the SAME three decorators in a DIFFERENT order, print the
        price again. They should NOT match. Figure out why, and write
        one sentence explaining it as a comment.
"""

from abc import ABC, abstractmethod


class Priceable(ABC):
    @abstractmethod
    def get_price(self) -> float:
        ...

    @abstractmethod
    def get_description(self) -> str:
        ...


class Book(Priceable):
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.title


class BookDecorator(Priceable):
    def __init__(self, wrapped: Priceable):
        self._wrapped = wrapped

    def get_price(self) -> float:
        return self._wrapped.get_price()

    def get_description(self) -> str:
        return self._wrapped.get_description()


# TODO: GiftWrapDecorator(BookDecorator)
#   get_price() -> self._wrapped.get_price() + 5
#   get_description() -> self._wrapped.get_description() + " + gift wrap"
class GiftWrapDecorator(BookDecorator):
    def get_price(self) -> float:
        return self._wrapped.get_price() + 5

    def get_description(self) -> str:
        return self._wrapped.get_description() + " + gift wrap"


# TODO: ExpressShippingDecorator(BookDecorator)
#   get_price() -> self._wrapped.get_price() + 10
#   get_description() -> self._wrapped.get_description() + " + express shipping"
class ExpressShippingDecorator(BookDecorator):
    def get_price(self) -> float:
        return self._wrapped.get_price() + 10

    def get_description(self) -> str:
        return self._wrapped.get_description() + " + express shipping"


# TODO: InsuranceDecorator(BookDecorator)
#   get_price() -> self._wrapped.get_price() * 1.02   (2% of whatever it receives)
#   get_description() -> self._wrapped.get_description() + " + insurance"
class InsuranceDecorator(BookDecorator):
    def get_price(self) -> float:
        return self._wrapped.get_price() * 1.02

    def get_description(self) -> str:
        return self._wrapped.get_description() + " + insurance"


if __name__ == "__main__":
    base = Book("Dune", 20.0)

    order_a = InsuranceDecorator(ExpressShippingDecorator(GiftWrapDecorator(base)))
    print(order_a.get_description(), "->", order_a.get_price())

    order_b = ExpressShippingDecorator(GiftWrapDecorator(InsuranceDecorator(base)))
    print(order_b.get_description(), "->", order_b.get_price())

    # TODO: are order_a's and order_b's prices the same? Why / why not?
    #       (one-sentence comment explaining it)

# each decorator only ever sees the price returned by whatever it directly wraps —
# it has no visibility into what's further inside or further outside the stack. 
# So a percentage-based decorator's result depends entirely on how much has already been added by the time it's reached in the chain.
# That's a real, general property of the Decorator pattern worth internalizing: 
# percentage-based (multiplicative) decorators are order-sensitive, while flat-fee (additive) decorators are commutative with each other — 
# swapping GiftWrap and ExpressShipping between themselves would never change the total, but swapping either of them with Insurance always can.