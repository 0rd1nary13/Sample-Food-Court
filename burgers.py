class Burger:
    def __init__(self, name, number, price):
        self.name = name
        self.number = 0
        self.price = price


class DeAnzaBurger(Burger):
    def __init__(self):
        super().__init__("De Anza Burger", 1, 5.25)


class BaconCheese(Burger):
    def __init__(self):
        super().__init__("Bacon Cheese", 2, 5.75)


class MushroomSwiss(Burger):
    def __init__(self):
        super().__init__("Mushroom Swiss", 3, 5.95)


class WesternBurger(Burger):
    def __init__(self):
        super().__init__("Western Burger", 4, 5.95)


class DonCaliBurger(Burger):
    def __init__(self):
        super().__init__("Don Cali Burger", 5, 5.95)
