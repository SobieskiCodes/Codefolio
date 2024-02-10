#===========================================================
#
#  Title:       Udderly Awesome Calculator
#  Author:      Justin Sobieski
#  Date:        1/18/2024
#  Description:
#       It will be a milk calculator.
#
#===========================================================

gallons_of_milk = 0

milk_data_dict = {
    "w": {
        "Milk Type": "Whole",
        "Price": "4.00"
    },
    "t": {
        "Milk Type": "2%",
        "Price": "3.50"
    },
    "s": {
        "Milk Type": "Skim",
        "Price": "3.00"
    }
}

# Input Section
milk_type = input("Enter the milk type (w=whole; t=2percent; s=skim): ")
if milk_type.lower() in milk_data_dict:
    print(f"Price per gallon: ${milk_data_dict[milk_type.lower()]['Price']}")
    gallons_of_milk = int(input("Enter the number of gallons of milk: "))
    total = float(milk_data_dict[milk_type.lower()]['Price']) * gallons_of_milk

# Output section
    print("Milk type purchased: {}".format(milk_data_dict[milk_type.lower()]['Milk Type']))
    print("Gallons purchased:   {}".format(gallons_of_milk))
    print("Cost per gallon:     ${:}".format(milk_data_dict[milk_type.lower()]['Price']))
    print("Total:               ${:.2f}".format(total))

else:
    print("Invalid milk type entered")

