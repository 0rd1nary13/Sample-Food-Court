class Student:
    def __init__(self):
        self.tax_rate = 0

    def get_tax_rate(self):
        return self.tax_rate


class Staff:
    def __init__(self):
        self.tax_rate = 0.09

    def get_tax_rate(self):
        return self.tax_rate 