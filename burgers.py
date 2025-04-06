class Burger:
    def __init__(self, name, number, price):
        self.name = name
        self.number = number
        self.price = price

    def __float__(self):
        # Required for sum() calculations
        return float(self.price)

