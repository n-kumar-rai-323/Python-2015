In Python, string formatting is a way to insert variables or values into strings. There are several methods to format strings:

1. Using f-strings (Python 3.6+)
This is the easiest and most readable method.

python
Copy
Edit
name = "Alice"
age = 20
print(f"My name is {name} and I am {age} years old.")
Output:

pgsql
Copy
Edit
My name is Alice and I am 20 years old.
2. Using str.format()
This method works in Python 2.7 and 3.x.

python
Copy
Edit
name = "Bob"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
You can also use index numbers:

python
Copy
Edit
print("My name is {0} and I am {1} years old. {0} likes Python.".format(name, age))
3. Using % Operator (Old Style)
This is an older method, similar to C-style formatting.

python
Copy
Edit
name = "Charlie"
age = 30
print("My name is %s and I am %d years old." % (name, age))
%s → String
%d → Integer
%f → Float
4. Formatting Numbers
You can format numbers with commas, decimals, etc.


price = 1234.56789
print(f"Price: {price:,.2f}")  # Adds comma and shows 2 decimal places

Price: 1,234.57