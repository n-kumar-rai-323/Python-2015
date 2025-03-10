# A tuple in Python is a collection of items that is:

# Ordered: The items have a defined order, and that order will not change.
# Immutable: Once a tuple is created, you cannot change, add, or remove items from it.
# Allowing Duplicates: Tuples can have duplicate values.

# A simple tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Tuple with different data types
mixed_tuple = (1, "Hello", 3.14, True)
print(mixed_tuple)

# Tuple with one item (add a comma)
single_item_tuple = (10,)
print(single_item_tuple)

# Without parentheses (Python will still consider it a tuple)
another_tuple = 1, 2, 3
print(another_tuple)


# Accessing Tuple Elements 
# Indexing (starts from 0)
print(my_tuple[0])    # Output: 1
print(my_tuple[-1])   # Output: 5 (last item)

# Slicing
print(my_tuple[1:4])  # Output: (2, 3, 4)
