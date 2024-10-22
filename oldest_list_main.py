# Make a list
entries = []

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

print(name)
print(age)

# Array to put the data in
# Add another entry
# Assume that the first entry is the oldest
# Add a function that compares a new entry to the oldest entry
# Print the oldest person in the list after it checks to see who is the oldest in the list