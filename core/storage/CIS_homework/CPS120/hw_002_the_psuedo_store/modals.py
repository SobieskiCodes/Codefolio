import random
from datetime import datetime, time
# Set a fixed price for simplicity, could be dynamic based on coffee attributes
# Function at 39: def order_and_pay_for_coffee(self, coffee):
coffee_price = 2.99


class Store:
    def __init__(self, store_name, store_opening_hour, store_closing_hour, low_stock_threshold, inventory_item_max_size, inventory_item_min_size):
        self.name = store_name
        # Assume store_opening_hour and store_closing_hour are integers representing the 24-hour clock
        self.opening_time = time(store_opening_hour, 0)  # opens at store_opening_hour:00
        if store_closing_hour == 24:
            # In Python, the time object's hour field is valid from 0 to 23
            # Set to one second before midnight
            self.closing_time = time(23, 59, 59)  
        else:
            self.closing_time = time(store_closing_hour, 0)  # closes at store_closing_hour:00

        self.inventory_item_max_size = inventory_item_max_size
        self.inventory_item_min_size = inventory_item_min_size

        # Initialize the coffee inventory with random values, that can be passed when creating the store.
        self.inventory = {
            size: {type: random.randint(self.inventory_item_min_size, self.inventory_item_max_size)
                   for type in ['regular', 'dark roast', 'decaf', 'flavored']}
            for size in ['small', 'medium', 'large']
        }
        self.low_stock_threshold = low_stock_threshold * self.inventory_item_max_size

    def is_open(self):
        current_time = datetime.now().time()
        # It probably would have been quicker to just do something like always_open=True
        if self.opening_time <= self.closing_time:
            # Normal scenario: store opens and closes on the same day
            return self.opening_time <= current_time < self.closing_time
        else:
            # Handle overnight scenario: store closes on the following day
            return current_time >= self.opening_time or current_time < self.closing_time
    
    # def restock_coffee(self, size, type, amount):
    #     # Restock a particular type of coffee, I'd like to extend this to require you to be a store employee
    #     if size in self.inventory and type in self.inventory[size]:
    #         self.inventory[size][type] += amount
    #         print(f"Restocked {amount} {size} {type} coffee.")
    #     else:
    #         print("Invalid coffee size or type for restocking.")

    def check_inventory(self):
        # Print the current inventory of coffee
        divider = ('-' * 21)
        print(f"\n{divider}\nCurrent inventory:\n{divider}")
        for size in self.inventory:
            for type in self.inventory[size]:
                print(f"{size} {type}: {self.inventory[size][type]}")
        print(f"{divider}\nEnd of inventory\n")

    def order_and_pay_for_coffee(self, coffee, current_balance):
        # Check if the store is open
        if not self.is_open():
            print("Sorry, the store is currently closed.")
            return
        
        # Check if the coffee is available in the inventory
        stock = self.inventory[coffee.size][coffee.type]
        if stock > 0:
            # Proceed with payment
            payment_processor = PaymentProcessor(self.name)
            new_balance, payment_successful = payment_processor.process_payment(coffee.price, current_balance)
            if payment_successful:
                # Deduct the coffee from the inventory after successful payment
                self.inventory[coffee.size][coffee.type] -= 1
                ending_string = coffee.add_ins if coffee.add_ins is not None else "love"
                print(f"\nOrder successfully placed for a {coffee.size} {coffee.type} coffee made with {', '.join(ending_string)}.")
                print(f"Thank you for your purchase! Your payment processed for ${coffee.price:.2f}. Your new balance is ${new_balance:.2f}.")
                # After updating the inventory, check for low stock and inform if necessary
                new_stock = self.inventory[coffee.size][coffee.type]
                if new_stock <= self.low_stock_threshold:
                    print(f"\n!! Alert: Low stock for {coffee.size} {coffee.type}. Only {new_stock} left. !!\n")
                else:
                    print(f"{new_stock} {coffee.size} {coffee.type} coffees remaining in stock.\n")
                return new_balance, True
            else:
                print(f"Payment denied: Insufficient funds, your current balance is {current_balance}.\n")
                return current_balance, False
        else:
            print(f"Sorry, the {coffee.size} {coffee.type} coffee is currently unavailable.")

class PaymentProcessor:
    def __init__(self, store_name):
        self.store_name = store_name

    def process_payment(self, amount, current_balance):
        funds_available = current_balance >= amount
        if funds_available:
            new_balance = current_balance - amount
            return round(new_balance), True
        else:
            return round(current_balance), False

class Coffee:
    def __init__(self, size, type, coffee_price, add_ins=None):
        self.size = size
        self.type = type
        self.price = coffee_price
        self.add_ins = add_ins

    def __repr__(self):
        return f"Coffee(size='{self.size}', type='{self.type}', add_ins={self.add_ins})"