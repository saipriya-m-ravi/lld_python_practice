"""
Lesson 4.6 - Strategy

Step 1: Read BadShippingCalculator. Adding a new shipping method means
        editing calculate_cost() itself -- the exact OCP smell from
        Lesson 2.2, just showing up again in a new place.
Step 2: Refactor into Strategy: an abstract ShippingStrategy, concrete
        strategies, and a ShippingCalculator context.
Step 3: The NEW part -- prove you can swap a strategy on an ALREADY
        EXISTING calculator object, live, via set_strategy(). Don't
        create a second calculator to do this.
"""

from abc import ABC, abstractmethod


class BadShippingCalculator:
    def calculate_cost(self, method: str, weight_kg: float) -> float:
        if method == "standard":
            return weight_kg * 2.0
        elif method == "express":
            return weight_kg * 5.0 + 10
        elif method == "overnight":
            return weight_kg * 10.0 + 25
        else:
            raise ValueError(f"Unknown shipping method: {method}")


# ============================================================
# TODO: Refactor.
#
# 1. ShippingStrategy(ABC) with an abstract calculate(self, weight_kg) -> float
# 2. StandardShipping, ExpressShipping, OvernightShipping -- same formulas
#    as BadShippingCalculator above, one per class
# 3. ShippingCalculator (the context):
#    - __init__(self, strategy: ShippingStrategy): store it
#    - set_strategy(self, strategy: ShippingStrategy): REPLACE the stored
#      strategy on this same object (this is the new piece -- not a new
#      constructor call, a mutation of an existing instance)
#    - calculate_cost(self, weight_kg: float) -> float: delegate to
#      self._strategy.calculate(weight_kg)
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight_kg) -> float:
        pass


class StandardShipping(ShippingStrategy):
    def calculate(self, weight_kg):
        return weight_kg * 2.0

class ExpressShipping(ShippingStrategy):
    def calculate(self, weight_kg):
        return weight_kg * 5.0 + 10

class OvernightShipping(ShippingStrategy):
    def calculate(self, weight_kg):
        return weight_kg * 10.0 + 25

class ShippingCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: ShippingStrategy):
        self._strategy = strategy
    
    def calculate_cost(self, weight_kg: float) -> float:
        return self._strategy.calculate(weight_kg)
# ============================================================


if __name__ == "__main__":
    calc = ShippingCalculator(StandardShipping())
    print(calc.calculate_cost(5))          
    calc.set_strategy(ExpressShipping())    
    print(calc.calculate_cost(5))        
    calc.set_strategy(OvernightShipping())  
    print(calc.calculate_cost(5))     
