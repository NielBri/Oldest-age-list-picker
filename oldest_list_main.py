import re

# Make a list
entries = []

# Loop 2 checks if the user wants to input another entry
while True:
    # Loop 4 is for checking if the name is only text
    while True:
        name = input("Please input name: ")
        if re.match(r"^[a-zA-Z .]+$", name):
            break
        else:
            print("Error! Invalid name.")


    # Loop 1 checks if the age is an integer and anything else will result into another input
    while True:
        # Age input
        try:
            age = int(input("Please input age: "))
            if 0 < age <= 120:
                break
            else:
                print("Error! Please input a valid age range (1-120)")
        except:
            print("Error! Please input again.")

    # Array to put the data in
    entries.append({
            "name" : name,
            "age" : age
        })

    # Loop 3 checks only if the input is yes or no
    while True:

        # Add another entry. Also added the .lower() to check whether capitalized or not
        another = (input("Add another entry? (Yes/No): ")).lower()

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
def oldest(entries):
    oldest_entry = entries[0]

# Add a function for the def that compares a new entry to the oldest entry

    # This function assigns the current entry in the list as new_age for the list entries[]
    for new_age in entries:

    # Compares the current entry (new_age) to the first entry (oldest_entry) and returns the oldest
        if new_age["age"] > oldest_entry["age"]:
            oldest_entry = new_age
    return oldest_entry

# Print the oldest person in the list after it checks to see who is the oldest in the list
# This checks the entries list if not empty
if entries:
    # This assigns oldest entry found in the list as oldest_entry
    oldest_entry = oldest(entries)
    print(f'The oldest person is {oldest_entry["name"]} with an age of {oldest_entry["age"]}')



# Fix the last print wherein if two or more people have the same highest age it should print all the people with it
