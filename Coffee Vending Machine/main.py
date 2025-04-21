class Coffee:
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_recipe(self):
        return self.recipe
    
class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return self.quantity
    
    def update_quantity(self, amount):
        self.quantity += amount

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount
    
    


    
        