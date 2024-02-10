#===========================================================
#
#  Title:       The Psuedo Store
#  Author:      Justin Sobieski
#  Date:        1/19/2024
#  Description:
#       A short program to determine the pay and taxes on a 
#       paycheck based on an hourly rate and number of hours
#       worked.
#
# Special notes: 
#       Insufficient funds are not handled well right now.
#       Checking the balance should be a function, it's not.
#       You may not start with enough money to buy a coffee.
#       I'd like to rework the functions to make them a 
#       little more concise, readable, and functional - 
#       I tried to combine a few things as I rushed / got stuck.
#===========================================================

import sys
import json
import random
from modals import Store, Coffee

def get_user_selection(options, prompt):
    # Display options in a formatted list
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print('\n')
    while True:
        try:
            choice = int(input("Enter your choice (number): "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")

# Function to ask user to create their coffee order
def create_coffee_order():
    # Define options
    sizes = ['small', 'medium', 'large']
    types = ['regular', 'dark roast', 'decaf', 'flavored']
    add_ins_options = ['sugar', 'cream', 'honey', 'cinnamon']
    price = 2.99 # you'd create a forumla here

    selected_size = get_user_selection(sizes, "Please select your coffee size:")
    selected_type = get_user_selection(types, "Please select your coffee type:")

    # Add-ins can have multiple selections, handle accordingly
    add_ins = []
    print("Please select your add-ins (type 'done' when finished):")
    for add_in in add_ins_options:
        response = input(f"Would you like some {add_in}? (y/n): ").lower()
        if response == 'y':
            add_ins.append(add_in)
        elif response == 'done':
            break  # Exit the loop if 'done' is entered

    # If no add-ins were selected, offer the 'none' option
    if not add_ins:
        add_ins.append('love')


    return Coffee(selected_size, selected_type, price, add_ins)

def save_balance(config, new_balance):
    config["card_balance"] = round(new_balance, 2)
    with open('config.json', 'w') as config_file:
        json.dump(config, config_file, indent=4)
    return new_balance

def main():
    # Read configuration and jokes from JSON file
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        
    version = config["version"]
    store_config = config["store_config"]
    # Create the store using the configuration from the JSON file
    store = Store(**store_config)
    current_balance = config["card_balance"]

    if not current_balance:
        new_balance = random.randint(3, 10)
        current_balance = new_balance
        save_balance(config, new_balance)

    welcome_message = (
        f"\nWelcome to {store_config['store_name']} {version}! "
        "Where every cup of coffee has its own story."
    )
    print(f"{welcome_message}")

    menu_actions = {
        "Buy a coffee": create_coffee_order,
        "Check inventory": store.check_inventory,
        "Quit": sys.exit
    }

    while True:
        if store.is_open():
            print("Feeling a bit perky? How about a joke?")
            print(f'-> {random.choice(config["jokes"])}\n')

            # Print the actions menu
            for i, (label, _) in enumerate(menu_actions.items(), start=1):
                print(f"{i}. {label}")

            user_choice = input("\nPlease enter your choice: ")
            chosen_action = list(menu_actions.values())[int(user_choice) - 1] if user_choice.isdigit() and int(user_choice) - 1 in range(len(menu_actions)) else None

            if chosen_action:
                if chosen_action == create_coffee_order:
                    coffee_order = chosen_action()  # Create the coffee order by calling/invoking the function by adding the () at the end
                new_balance, payment_successful = store.order_and_pay_for_coffee(coffee_order, current_balance)
                if payment_successful:
                    current_balance = new_balance  # Update the current balance variable
                    save_balance(config, new_balance)

                else:
                    chosen_action()  # Call the chosen action ^

                if chosen_action == "quit":
                    print("Thank you for visiting! Have a great day.")
                    break
            else:
                print("Invalid choice. Please select from the available options.")
        else:
            print("Sorry, the store is currently closed. Please come back during our open hours.")
            break 



if __name__ == "__main__":
    main()
