# In Python, a list is a collection of items that is ordered, changeable (mutable), and allows duplicate elements. You can store different data types in a list, such as numbers, strings, and even other lists.
# Creating a list 

# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed = [1, "hello", 3.14, True]


# Common List Methods 
# 1. append() - Add an item to the end of the list. 

fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# 2. insert() - Inserts an item at a specific position.

fruits.insert(1, "mango")
print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'orange']

# 3. extend() -Adds elements from another list. 
fruits.extend(["grape", "melon"])
print(fruits)  # ['apple', 'mango', 'banana', 'cherry', 'orange', 'grape', 'melon']

# 4. remove() - Removes the first matching element.
fruits.remove("banana")
print(fruits)  # ['apple', 'mango', 'cherry', 'orange', 'grape', 'melon']

# 5.pop() -Removes an item at the given index (default is the last item). 
fruits.pop()        # Removes 'melon'
fruits.pop(1)       # Removes 'mango'
print(fruits)       # ['apple', 'cherry', 'orange', 'grape']

# 6.clear() - Removes all items from the list. 
fruits.clear()
print(fruits)  # []

# 7. index() - Returns the index of the first occurrance of an item. 
numbers = [10, 20, 30, 40, 50]
print(numbers.index(30))  # 2

# 8.count() - Returns the number of occurrences of an item. 
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # 3


# 9.sort() -Sorts the list in ascending order(can sort descanding with reverse=True)
numbers.sort()
print(numbers)  # [1, 2, 2, 2, 3, 4]

numbers.sort(reverse=True)
print(numbers)  # [4, 3, 2, 2, 2, 1]

# 10. reverse() - Reverses the order of the list 
numbers.reverse()
print(numbers)  # [1, 2, 2, 2, 3, 4]

# copy() - Creates a shallow copy of the list
new_list = numbers.copy()
print(new_list)  # [1, 2, 2, 2, 3, 4]

# Example:Combining Methods
my_list = [3, 1, 4, 1, 5, 9]
my_list.append(2)
my_list.sort()
my_list.reverse()
print(my_list)  # [9, 5, 4, 3, 2, 1, 1]
