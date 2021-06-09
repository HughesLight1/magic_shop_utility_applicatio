from models.alchemist import Alchemist

class Item:
    def __init__(self, name, type, description, quantity, cost, price, alchemist, id = None):
        self.name = name
        self.type = type
        self.description = description
        self.quantity = quantity
        self.price = price
        self.cost = cost
        self.alchemist = alchemist
        self.id =id

    def low_stock(self):
        low_quantity= 3
        if self.quantity <= low_quantity and self.quantity >0:
            return True
        else:
            return False

    def out_of_stock(self):
        if self.quantity <= 0:
            return True
        else:
            return False
    
    def calculate_total(self):
        total = self.price - self.cost
        return total