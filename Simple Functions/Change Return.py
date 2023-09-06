"""
The user enters a cost and then the amount of money given.
The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
"""
import decimal

# Get user input for cost and the amount given
cost = decimal.Decimal(input("Enter the cost: "))
amount_given = decimal.Decimal(input("Enter the amount given: "))

# Calculate change
change = amount_given - cost

# Convert change to cents
change_cents = int(change * 100)

# Calculate number of quarters, dimes, nickels, and pennies needed for change
quarters = change_cents // 25
change_cents %= 25

dimes = change_cents // 10
change_cents %= 10

nickels = change_cents // 5
change_cents %= 5

pennies = change_cents

# Print results
print("Change:", change)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
