# Basic Conditional Statement 

x = 10 
if x > 5:
    print("X is grater then 5")
elif x == 5:
    print("X is equal to 5")
else:
    print("X is less then 5")

# Logical Operators in Conditions

a = 10
b = 20
if a > 5 and b > 15:
    print("Both conditions are true")
if a > 15 or b > 15:
    print("At lest one condition is true")
if not (a ==10):
    print("a is not equal to 10")


# Ternary Conditional Operator 
age = 18 
status = "adult" if age>= 18 else "Minor"
print(status)


# Using in and not in for condition checking 
fruits = ["apple", "banana", "cherry"]

if "apple" in fruits:
    print("Apple is in the list")

if "grape" not in fruits:
    print("Grape is not in the list")