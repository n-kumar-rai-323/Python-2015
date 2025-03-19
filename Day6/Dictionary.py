student ={
     "name" : "Alisha",
    "age" : 22,
    "grade": "A+"
}

# [{
#     "name" : "Nishan",
#     "age" : 20,
#     "grade": "A"
# },
# ]
# Accessing Values 

# print(student["name"])
# print(student.get("age"))

# Modifying a Dictionary 
# student["age"] = 21
# student["subject"] = "Computer Science"


# Removing Elements 
# student.pop("grade")
# del student["age"]


print("Looping Through a Dictionary")
for key, value in student.items():
    print(key, ":", value)