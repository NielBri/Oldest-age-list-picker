# Make a list
entries = []

# Loop 2 checks if the user wants to input another entry
while True:
    # Name input
    name = input("Please input name: ")

    # Loop 1 checks if the age is an integer and anything else will result into another input
    while True:
        # Age input
        try:
            age = int(input("Please input age: "))
            # This breaks Loop 1
            break
        except:
            print("Error! Please input again.")

    # Array to put the data in
    entries.append({
            "name" : name,
            "age" : age
        })

    # Add another entry. Also added the .lower() to check whether capitalized or not
    another = (input("Add another entry? (Yes/No): ")).lower()

    # Loop 3 checks only if the input is yes or no
    while True:
        if another == "yes":
            # This breaks Loop 3 and allows the user to put another entry
            break
        elif another == "no":
            # This also breaks Loop 3 and goes to the Loop 2 break
            break
        else:
            print("Error! Please input again.")

    # This checks the input if no like in Loop 3 and continues to break Loop 2
    if another == "no":
        # Breaks Loop 2
        break

# Assume that the first entry is the oldest
# Add a function that compares a new entry to the oldest entry
# Print the oldest person in the list after it checks to see who is the oldest in the list