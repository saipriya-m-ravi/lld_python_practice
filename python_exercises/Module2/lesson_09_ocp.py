"""
Lesson 2.2 - Open/Closed Principle (OCP)

Step 1: Read BadPricingService below. Do not change it yet.
Step 2: Imagine the library adds a new membership tier, "veteran",
        with a 30% discount. Notice you'd have to edit calculate_price()
        itself to support it -- that's the OCP violation.
Step 3: Refactor so adding a new tier means adding a new class,
        with ZERO edits to the code that calculates a final price.
"""


class BadPricingService:
    def calculate_price(self, base_price, member_type):
        if member_type == "regular":
            return base_price
        elif member_type == "student":
            return base_price * 0.85       # 15% off
        elif member_type == "senior":
            return base_price * 0.80       # 20% off
        elif member_type == "premium":
            return base_price * 0.70       # 30% off
        else:
            raise ValueError(f"Unknown member_type: {member_type}")


from abc import ABC, abstractmethod


class DiscountPolicy(ABC):       
    @abstractmethod
    def apply(self, base_price):
        pass


class Regular(DiscountPolicy):       
    def apply(self, base_price):
        return base_price


class Student(DiscountPolicy):        
    def apply(self, base_price):
        return base_price*0.85


class Senior(DiscountPolicy):       
    def apply(self, base_price):
        return base_price*0.80 


class Premium(DiscountPolicy):       
    def apply(self, base_price):
        return base_price*0.70 


class Veteran(DiscountPolicy):
    def apply(self, base_price):
        return base_price*0.60


class PricingService:
    def calculate_price(self, base_price, discount_policy):
        return discount_policy.apply(base_price)
# ============================================================
# TODO: Refactor.
#
# 1. Define an abstract base (or just a shared-interface convention)
#    e.g. DiscountPolicy, with a method like apply(self, base_price) -> float
# 2. One concrete class per tier: RegularDiscount, StudentDiscount,
#    SeniorDiscount, PremiumDiscount -- each implements apply() with
#    its own percentage.
# 3. Rewrite PricingService so it no longer branches on a string at all --
#    it should accept a discount policy object and just call .apply() on it.
#    (This is the same "inject a swappable behavior object" idea from
#    Lesson 1.6's NotificationSender -- same shape, different use case.)
# 4. Prove OCP holds: add a brand new VeteranDiscount (30% off) at the
#    bottom of the file WITHOUT touching PricingService or any existing
#    discount class.
# ============================================================


if __name__ == "__main__":
    pass
    # TODO: create a PricingService (however you've designed it)
    # TODO: calculate a $100 book's price under student, senior, premium,
    #       and your new veteran discount -- print each result
    ps = PricingService()
    print(ps.calculate_price(100, Student()))
    print(ps.calculate_price(100, Senior()))
    print(ps.calculate_price(100, Premium()))
    print(ps.calculate_price(100, Veteran()))
