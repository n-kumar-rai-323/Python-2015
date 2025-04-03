print("List Print")
num = [2,3,4,5,6,7,8]
for i in num:
    print(i)


print("Tuple print")

num2 = (2,3,4,5,6,7)
for i in num2:
    print(i)



print("Dictionary Print")

person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "hobbies": ["reading", "hiking", "coding"],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}

print("Print key only")
for key in person:
    print(key)
print("value only")
for key in person.values():
    print(key)

print("Print key and value")
for key, value in person.items():
    print(f"{key}:{value}")