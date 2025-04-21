from Coffee import coffee
from Ingredient import ingredient

class coffeeMachine:
    _instance = None

    def __init__(self):
        if coffeeMachine._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            coffeeMachine._instance = self
            self.coffee_menu = []
            self.ingredients = {}
            self._initialize_ingredients()
            self._initialize_coffee_menu()

    @staticmethod
    def get_instance():
        if coffeeMachine._instance is None:
            coffeeMachine()
        return coffeeMachine._instance
    
    def _initialize_coffee_menu(self):
        espresso_recipe = {
            self.ingredients["Coffee"]: 1,
            self.ingredients["Water"]: 1
        }
        self.coffee_menu.append(coffee("Espresso", 2.5, espresso_recipe))

        chai_recipe = {
            self.ingredients["Indian chai patti"]: 1,
            self.ingredients["Milk"]: 2,
            self.ingredients["Masala"]: 1
        }
        self.coffee_menu.append(coffee("Chai", 5.2, chai_recipe))

        cappuccino_recipe = {
            self.ingredients["Coffee"]: 1,
            self.ingredients["Water"]: 1,
            self.ingredients["Milk"]: 1
        }
        self.coffee_menu.append(coffee("Cappuccino", 3.0, cappuccino_recipe))

    def _initialize_ingredients(self):
        self.ingredients["Coffee"] = ingredient("Coffee", 10)
        self.ingredients["Water"] = ingredient("Water", 10)
        self.ingredients["Milk"] = ingredient("Milk", 10)
        self.ingredients["Indian chai patti"] = ingredient("Indian chai patti", 10)
        self.ingredients["Masala"] = ingredient("Masala", 10)

    def display_menu(self):
        print("Coffee Menu:")
        for coffee in self.coffee_menu:
            print(f"{coffee.get_name()} - ${coffee.get_price()}")

    def select_coffee(self, coffee_name):
        for coffee in self.coffee_menu:
            if coffee.get_name().lower() == coffee_name.lower():
                return coffee
        return None
    
    def dispense_coffee(self, coffee, payment):
        if payment.get_amount() >= coffee.get_price():
            if self._has_enough_ingredients(coffee):
                self._update_ingredients(coffee)
                print(f"Dispensing {coffee.get_name()}...")
                change = payment.get_amount() - coffee.get_price()
                if change > 0:
                    print(f"Please collect your change: ${change}")
                else:
                    print(f"Insufficient ingredients to make {coffee.get_name()}")

            else:
                print(f"Insufficient ingriedents to make {coffee.get_name()}")

        else:
            print(f"Insufficient payment for {coffee.get_name()}")

    def _has_enough_ingredients(self, coffee):
        for ingredient, required_quantity in coffee.get_recipe().items():
            if ingredient.get_quantity() < required_quantity:
                return False
        return True

    def _update_ingredients(self, coffee):
        for ingredient, required_quantity in coffee.get_recipe().items():
            ingredient.update_quantity(-required_quantity)
            if ingredient.get_quantity() < 3:
                print(f"Low inventory alert: {ingredient.get_name()}")

    

    






    



    
        