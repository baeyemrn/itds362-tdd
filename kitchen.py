class Quantity:
    def __init__(self, amount, unit,):
        self.amount = amount
        self.unit = unit
       

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def __eq__(self, other):
        return (
        self.amount == other.amount
        and self.unit == other.unit
     )

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"

    def plus(self, other):
        return Sum(self, other)

    
class Converter:
    def reduce(self, expression, unit):
        return expression.reduce(unit)

    def convert(self, quantity, unit):
        if quantity.unit == unit:
            return quantity

        if quantity.unit == "oz" and unit == "g":
            return Quantity(quantity.amount * 28.35, "g")

        raise ValueError("Unknown conversion")

class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def reduce(self, unit):

        converter = Converter()

        left = converter.convert(self.left, unit)
        right = converter.convert(self.right, unit)
        return Quantity(
            left.amount + right.amount,
            unit
        )

    def times(self, multiplier):
        return Sum(
            self.left.times(multiplier),
            self.right.times(multiplier),
        )
  
    
