# lambda / Anonymous function 

# A lambda function in Python is a small, anonymous function defined with the 
# lambda keyword. It's often called an "anonymous" function because it doesn't 
# have a formal name like functions defined with def

add = lambda a , b : a +b
print(add(3 , 5))

a = [(3,6), (5,6), (1,2),(2,1)]


a.sort(key=lambda data:data[1])
print(a)
# higher order functions
# if a function takes another function as a paramet
# it is a higher order function

# map(), filter(), reduce() are the examples of higher order function

#map
a = [1,2,3,4,5]
def multiple_of_two(data):
    return data * 2
            # Function      #iterator 
result =map(multiple_of_two, a)
print(list(result))


#filter()
a = [1,2,3,4,5,6,7]
# def get_even_nums(data):
#     return data % 2==0

result = filter(lambda data: data %2==0,a)
# result = filter(get_even_nums, a)
print(list(result))


students = [
    {
        "name": "Nishan",
        "age":28
    },
    {
        "name": "jon",
        "age":29
    },
    {
        "name": "gita",
        "age":23
    },
    {
        "name": "Nikita",
        "age":94
    },
]

result = filter( lambda data: data["age"] >=25,students)
print(list(result))


a = [1,5,3,15,9,10]

result = map(lambda x:x % 5 ==0, a)
print(list(result))

#Reduce() function
a =[1,2,3,4,5]
from functools import reduce
result = reduce( lambda x , y: x + y, a)
print(result)