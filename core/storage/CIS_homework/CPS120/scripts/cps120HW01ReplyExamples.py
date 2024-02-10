# initializing a few variables to display first on python tutor, note the global frame.
# http://tinyurl.com/5d2xzwd5
my_number_example = 0.0
my_other_example = float()

# Comment: "Warning: It looks like you are running this program in IDLE. The progress animation will not display.
# Best to assume that the user of your product has the most generic version of Python. No Points Off.
# That was the assumption made, here is a practicle example you can run in IDLE and repl.it to verify.
divider = ('-' * 25)
print(f'{divider}\nWe will now display part 1: \n{divider}')
try: 
    import sys
    if not "idlelib" in sys.modules:
        print("you arent in idle! :)")
        
    else:
        color = sys.stdout.shell
        color.write("IDLE DETECTED", "ERROR")
        color.write("You are in idle!\n", "KEYWORD")
except Exception as e:
    print(f"Importing sys likely isn't support on this machine, python tutor? Moving past this example. \n{e}")

print(f'{divider} \nWe will now display part 2: \n{divider}')
# Comment: "Critical Issue: This program is an infinite loop. That is a logic error. No points off as you were going for Bonus but take care in future.
user_input = input('The loop was created to be infinite by intention, type "quit" to exit: ')
while user_input != "quit":
    user_input = input('Put any input in or type "quit" to exit: ')
    print(f'You typed in: {user_input}')
    if user_input == "quit":
        break

print(f'{divider} \nWe will now display part 3: \n{divider}')
# Comment: "Line up the $'s signs and the decimal points by using the format command given.""
# One small example of why f-strings are better than format: https://www.python.org/dev/peps/pep-0498/
# Not only can it format better, it has more features and is faster.
my_number = 3.14
my_string = "example: "
# ${my_number:^} 
try:
	 # Attempt to concatenate a string and a number (which will cause a TypeError) in anything not Python 3.6+ with f-strings
	print("my_string: " + my_string + "my_number: " + my_number)
except TypeError: # you obviously still can't math with strings and numbers, but you don't have to be tedious.
	print("This only works in Python 3.6+ with f-strings")

except Exception as e:
	print(f"something went wrong {e}")
	
finally:
    for number in range(0, len(my_string)):
        total_value = f"{number * my_number:.2f}"
        print(f'{my_string:>5} {number} * {my_number} = ${total_value:^10}')



print(f'{divider} \nWe will now display part 4: \n{divider}')
# Comment: "This is not the correct way to initialize a variable:"
# Though I do understand why it matters when it comes to java c++
conditions = [
    (float() == 0.0, "float() is not equal to 0.0"),
    (list() == [], "list() is not equal to []"),
    (str() == '', "str() is not equal to ''"),
    (float() == 5.0, "float() is not equal to 5.0"),
	(int() == 0, "int() is not equal to 0"),
	(int() == 12, "int() is not equal to 12")
]

for i, (condition, message) in enumerate(conditions):
    try:
        print(f"Asserting condition {i+1} is True: {condition}")
        assert condition, message
    except AssertionError as error:
        print(f"Assertion {i+1} failed: {error}")



# https://stackoverflow.com/questions/2347265/why-does-behave-unexpectedly-on-lists
# =+ is good, but be careful with lists / sequences