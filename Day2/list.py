# list

l = list()
print(type(l))
list = [] # Empty list can aslo be created in this way 
print(type(list))


# list are heteregenous data type 
Many = [1, "hello", [5,6,7], (1,2,3)]
print(Many)


#Accessing list elements
# List indexing starts from 0 for forward indexing and -1 for backward indexing 

print(Many[0])
print(Many[-1])
print(Many[3][2])


Many[3]= 10

# Slicing in list 
a= [0,1,2,3,4,5,6,7,8,9,10]
print(a[:])
print(a[:6]); print(a[0:6])

print(a[5:])

print(a[1:8])

# Negative Indexing 
print(a[:-4])
print(a[-5:])
print(a[-6:-2])
print(a[-6: -8])# its give empty list 

# List Operations 
# Concatenates + 
a = [1,2,3,4]
b = [5,6,7,8]
print(a+b) # This concatenates tow lists 

print(a)
print(b)


#Repetition with * operator (broadcast)

print(2 in a )
print(5 not in b)

#Operation
#Methods: Method are the functions which are compulsarily called by an object 
a.append(8)
print(a)
result = a.append("Nishan")
print(a)
print(result) #None

a.extend(b)
print(a)

# insert
a.insert(0,0)
print(a)
# remove
a.remove(4)
print(a)
#Bulit-in Function



# In Python, a list is a collection of items that are ordered, changeable (mutable), and allow duplicate values. Lists are created using square brackets [].
# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)


# Key Features:
# Ordered: Items have a defined order.
# Mutable: You can change, add, or remove items.
# Allows Duplicates: Lists can have the same item more than once.

# Common Operations: 
# 1. Access Items: 
# Using index (starts from 0)
print(my_list[0])   # Output: 1
print(my_list[-1])  # Output: 5 (last item)


# 2. Change Items 
my_list[1] = 20
print(my_list)  # Output: [1, 20, 3, 4, 5]

# 3. Add Items:
# Add at the end
my_list.append(6)
# Add at a specific position
my_list.insert(2, 15)
print(my_list)  # Output: [1, 20, 15, 3, 4, 5, 6]

# 4. Remove Items: 
# Remove by value
my_list.remove(20)
# Remove by index
del my_list[0]
# Remove last item
my_list.pop()
print(my_list)
