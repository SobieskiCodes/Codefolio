#===========================================================
#
#  Title:       Paycheck Calculator
#  Author:      Justin Sobieski
#  Date:        1/17/2024
#  Description:
#       A short program to determine the pay and taxes on a 
#       paycheck based on an hourly rate and number of hours
#       worked.
#===========================================================


# Imports
import time
import sys
from typing import List


# Declaration of Variables
hourly_rate = float()
hours_worked = float()
input_command = str()
commands_list = list()
prettify_dict = dict()
user_first_name = str()


# Input Section
def process_user_input() -> str:
    """
    Prompts the user to input hourly rate and number of hours worked. If either input is 'quit', 
    the function returns 'quit'. If inputs are valid numbers, it processes the paycheck. 
    If inputs are invalid, it returns an error message.

    The function uses 'validate_user_input' to check the validity of inputs 
    and 'process_paycheck' to calculate the paycheck details if inputs are valid.

    Returns:
    str: A string representing the result of the operation. It can be 'quit', 
         the result of 'process_paycheck', or an error message.

    Example:
    >>> process_user_input()
    Enter your hourly rate: 20
    Enter the number of hours worked: 40
    (returns the result of process_paycheck)

    >>> process_user_input()
    Enter your hourly rate: quit
    'quit'
    """
    hourly_rate = input("Enter your hourly rate: ")
    if hourly_rate.lower() == 'quit':
        return 'quit'

    hours_worked = input("Enter the number of hours worked: ")
    if hours_worked.lower() == 'quit':
        return 'quit'

    if validate_user_input([hourly_rate, hours_worked]):
        return process_paycheck(float(hourly_rate), float(hours_worked))
    else:
        print("Invalid input. Please enter valid numbers, ie `12.1` or `40`.")



# Processing/Calculations Section
def process_paycheck(hourly_rate: float, hours_worked: int) -> dict:
    """
    Calculates the gross pay, federal tax, FICA tax, state tax, and net pay for a given hourly rate and hours worked.

    Parameters:
    hourly_rate (int): The hourly rate of pay. Expected to be an integer representing the rate in dollars.
    hours_worked (float): The number of hours worked. Can be a float to accommodate partial hours.

    Returns:
    dict: A dictionary containing the gross pay, federal tax, FICA tax, state tax, and net pay. 
          Each of these is represented as a key-value pair in the dictionary, with the keys being 
          'gross_pay', 'federal_tax', 'fica_tax', 'state_tax', and 'net_pay'.

    Example:
    >>> process_paycheck(25, 40)
    {'gross_pay': 1000, 'federal_tax': 200, 'fica_tax': 76, 'state_tax': 50, 'net_pay': 674}
    """
    gross_pay = float(hourly_rate) * int(hours_worked)
    federal_tax = gross_pay * 0.15
    fica_tax = gross_pay * 0.0765
    state_tax = gross_pay * 0.0435
    net_pay = gross_pay - federal_tax - fica_tax - state_tax
    prettify_dict = {"gross_pay": gross_pay, "federal_tax": federal_tax, "fica_tax": fica_tax, "state_tax": state_tax, "net_pay": net_pay}
    return create_prettier_text(prettify_dict)


def validate_user_input(user_input_list: List[int]) -> bool:
    """
    Validates a list of user inputs to ensure each element is an integer. 
    This function is designed to verify that all elements in the list can be used as valid digits 
    in both integer and float formats for subsequent processing.

    The function displays a simple progress animation during the validation process.

    Parameters:
    user_input_list (List[int]): A list of integers. The function will check each element in this list.

    Returns:
    bool: True if all elements in the list are integers, False otherwise.

    Example:
    >>> validate_user_input([1, 2, 3, 4])
    Validating input:
    [■■■■■■■■■■]
    True

    >>> validate_user_input([1, 'a', 3, 4.5])
    Validating input:
    [■■■■■■■■■■]
    False
    """
    if not "idlelib" in sys.modules:
        print("Validating input:")
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")
    else:
        print('\n')
        color = sys.stdout.shell
        color.write("Warning: ", "ERROR")
        color.write("It looks like you are running this program in IDLE. The progress animation will not display.\n", "KEYWORD")

    return all(is_valid_number(user_input) for user_input in user_input_list)


def is_valid_number(value: str) -> bool:
    """
    Checks if the provided string value can be converted to a float.

    Parameters:
    value (str): The string to check.

    Returns:
    bool: True if the string can be converted to a float, False otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def create_prettier_text(prettify_dict: dict) -> list:
    """
    Formats the keys and values from a dictionary into a list of strings. Keys are converted 
    to title case unless they contain 'fica', in which case they are converted to upper case. 
    Values are formatted as currency.

    Parameters:
    prettify_dict (dict): A dictionary where keys are descriptive strings (possibly with underscores)
                          and values are numerical.

    Returns:
    list: A list of strings with each key-value pair formatted as 'Key: $Value'.

    Example:
    >>> create_prettier_text({'gross_pay': 848.80, 'fica_tax': 64.93})
    ['Gross Pay: $848.80', 'FICA TAX: $64.93']
    """
    temp_string_output_list = []
    for key, value in prettify_dict.items():
        # Replace underscores with spaces and convert to lower case
        key_formatted = key.replace('_', ' ').lower()

        # Convert to title case unless the key contains 'fica', then convert to upper case
        if 'fica' in key_formatted:
            key_formatted = f"{key_formatted.split(' ')[0].upper()} {key_formatted.split(' ')[1].title()}"
        else:
            key_formatted = key_formatted.title()

        # Append the formatted string to the list
        temp_string_output_list.append(f"{key_formatted}: ${value:.2f}")

    return temp_string_output_list


# Output Section
def client_output(final_output: List[str]):
    """
    Prints a formatted receipt-style output of each string in a given list. 
    This function is useful for displaying a list of formatted strings in a clean, 
    organized, and professional manner.

    Parameters:
    final_output (List[str]): A list of strings, each representing a line item in the receipt.

    Example:
    >>> client_output(['Gross Pay: $848.80', 'Federal Tax: -$127.32', 'FICA Tax: -$64.93', 'State Tax: -$36.92', 'Net Pay: $619.62'])
    -------------------------------
        PAYCHECK SUMMARY
    -------------------------------
        Gross Pay: $848.80
        Federal Tax: -$127.32
        FICA Tax: -$64.93
        State Tax: -$36.92
        Net Pay: $619.62
    -------------------------------
    Thank you for your hard work!
    """
    divider = "-" * 31
    header = f"\n\n{divider}\n{'PAYCHECK SUMMARY':^{len(divider)}}\n{divider}"
    body = "\n".join(f"{result:>5}" for result in final_output)
    footer = f"{divider}\nThank you for your hard work!\n"
    print(f"{header}\n{body}\n{footer}")
    input_command = input("Press Enter to continue")


# Main menu
def main_menu():
    """
    Main interface for the paycheck calculator program. 

    The function welcomes the user and prompts for their first name. It then enters a loop, 
    processing user inputs for paycheck calculations until the user chooses to quit.

    The function relies on 'process_user_input' to handle the input processing and 
    'client_output' to display the results.
    """
    welcome_string = "Type 'quit' to quit at anytime.\nLet's start with your first name.\n"
    print(welcome_string)

    user_first_name = input("Enter your first name: ")

    if user_first_name.lower() == 'quit':
        print("Goodbye.")
        sys.exit()

    print(f"Welcome {user_first_name.capitalize()}, to my paycheck calculator.\n")

    while True:
        input_command = process_user_input()
        if input_command:
            if input_command == "quit":
                print(f"Goodbye, {user_first_name}.")
                break
            else:
                client_output(input_command)
        

main_menu()


