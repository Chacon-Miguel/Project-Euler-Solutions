# defines function that converts a quantity of feet to inches
def feet_to_inches(feet):
    # Displays the result and formats the number to 6 significant figures
    print(feet, "feet in inches is", format(feet*12, 'g'))
# Calls the function and prompts the user the user to enter a number of feet
feet_to_inches(float(input("Enter a number of feet: ")))