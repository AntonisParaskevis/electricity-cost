while True:
    # Prompt the user to enter the appliance's power usage in watts
    watts = input("Enter the appliance's power usage in watts\n")
    
    # Check whether the user's input is valid (in this case, a positive integer). If the user has entered a letter, a punctation mark, a symbol, a non-integer number, zero, or a negative number, prompt them to enter a valid input
    if not watts.isdigit() or int(watts) <= 0:
        print("Invalid entry, please enter an integer greater than zero.")
        continue
    else:
        # Convert the user's input to an integer, as the input itself is a string by default
        watts = int(watts)
        break

while True:
    try:
        # Prompt the user to enter the appliance's usage hours
        hours = float(input("Enter the number of usage hours\n"))
        
        # If the user has entered either zero or a negative number, prompt them to enter a valid input
        if hours <= 0:
            print("Invalid entry, please enter a number greater than zero.")
            continue
        break
    except ValueError:
        # If the user has entered a non-numerical input, prompt them to enter a valid input
        print("Invalid entry, please enter a number greater than zero.")

# Same for the kw/h price
while True:
    try:
        kwh_price = int(input("Enter the kw/h price in cents. For example, if the kw/h costs $0.09, simply enter 9\n"))
        
        if kwh_price <= 0:
            print("Invalid entry, please enter an integer greater than zero.")
            continue
        break
    except ValueError:
        print("Invalid entry, please enter an integer greater than zero.")

# Calculate the electricity cost, using the user's input
cost = (watts * hours) / 1000 * kwh_price

# Display the electricity cost, rounded to 2 decimals
print("Electricity cost: $" + str(round(cost, 2)) + ".")

# In the end, prompt the user to press Enter, in order to exit the program
input("Press Enter to exit the program")