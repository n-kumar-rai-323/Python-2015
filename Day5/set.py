# In Python, a set is an unordered collection of unique items. Sets are useful when you want to store multiple items without duplicates.
# Using curly braces
my_set = {1, 2, 3, 4, 5}

# Using the set() function
another_set = set([4, 5, 6, 7])

# Key Features of Sets
# No duplicates: Each element is unique.
# Unordered: The order of items is not guaranteed.
# Mutable: You can add or remove items.

# Basic Operations
# 1.Adding Elements: 
my_set.add(6)      # Adds 6 to the set
my_set.update([7, 8])  # Adds multiple elements

# 2.Removing Elements:
my_set.remove(2)   # Removes 2 (raises error if not found)
my_set.discard(3)  # Removes 3 (no error if not found)
my_set.pop()       # Removes a random item
my_set.clear()     # Removes all items

# 3. Set Operations: 
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union = set1 | set2          # {1, 2, 3, 4, 5}
intersection = set1 & set2   # {3}
difference = set1 - set2     # {1, 2}
symmetric_diff = set1 ^ set2 # {1, 2, 4, 5}

# 4. Checking Membership 
print(3 in my_set)    # True
print(9 not in my_set)  # True
