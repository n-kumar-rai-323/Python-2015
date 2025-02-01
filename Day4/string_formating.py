name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")



name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))


name = "Charlie"
age = 30
print("My name is %s and I am %d years old." % (name, age))


# %s → String
# %d → Integer
# %f → Float


price = 1234.56789
print(f"Price: {price:,.2f}")  # Adds comma and shows 2 decimal places
