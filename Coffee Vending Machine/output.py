from main import coffeeMachine
from Payment import payment

class Output:
    @staticmethod
    def run():
        coffee_machine = coffeeMachine.get_instance()

        # Display coffee menu
        coffee_machine.display_menu()

        # Simulate user requests
        espresso = coffee_machine.select_coffee("Espresso")
        coffee_machine.dispense_coffee(espresso, payment(3.0))

        cappuccino = coffee_machine.select_coffee("Cappuccino")
        coffee_machine.dispense_coffee(cappuccino, payment(3.5))

        chai = coffee_machine.select_coffee("Chai")
        coffee_machine.dispense_coffee(chai, payment(4.0))


if __name__ == "__main__":
    Output.run()