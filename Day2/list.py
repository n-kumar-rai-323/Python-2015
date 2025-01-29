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