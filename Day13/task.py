s = "All the occurrences of a specified character in a given string"
new_s =" "
char = input("Enter the character")
for i in s:
    if i.lower() == char.lower():
        continue
    new_s +=i

print(new_s)


a = [4,2,3,1,2,5]
s = ""
for i in a:
    s += f"{i}"

print(s)

n = input("Enter a number")
reverse = n[::-1]
print("Palindrome") if n== reverse else print("Not Palindrome") 

#Treating n as integer

n = int(input("Enter a number"))
b=n
reverse =0
while n !=0:
    remainder = n %10
    reverse = reverse *10 + remainder
    n =n//10
print(reverse)