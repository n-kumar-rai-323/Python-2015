a = (1 ,2, 3)

b = [1, 2, 3]

b[1]=5
print(b)

# a[1]=8 This is not possible
print(a)

# Integer,float, Tuple, String are immutable datatypes in python 
# list, Dictionary and set are the mutable datatyps in python 

#Number : integer, float and complex
print(type(4))


# >>> import os
# >>> clear = lambda:os.system("cls")


n1= 3e2 # This is 3 * 10 ** 2. it gives 300.0
print(n1)

n2= 3e-2 # This is 3 * 10 ** -2. it gives 0.03
print(n2)


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