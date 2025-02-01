>>> text = "Hello World"
>>> print(text.upper())
HELLO WORLD
>>> print(text.lower())
hello world
>>> print(text.capitalize())
Hello world
>>> print(text.title())
Hello World
>>> text ="     Hello World    "
>>> print(text.strip())
Hello World
>>> print(text.lstrip())
Hello World
>>> print(text.rstrip())
     Hello World
>>> text = "I love python"
>>> print(text.replace("python", "java"))
I love java
>>> text = "apple,banana,cherry"
>>> fruits=text.split(",")
>>> fruits
['apple', 'banana', 'cherry']
>>> joined="_".join(fruits)
>>> print(joined)
apple_banana_cherry
>>> text ="Hello World"
>>> print(text.find("World"))
6
>>> print(text.find("Python")
... )
-1
>>> text = "Hello World"
>>> print(text.startswith("Hello"))
True
>>> print(text.endswith("World"))
True
>>> print("Hello".isalpha())
True
>>> print("12345".isdigit())
True
>>> print("Hello123".isalnum())
True
>>> text = "banana"
>>> print(text.count("a"))
3
>>> num = "42"
>>> print(num.zfill(5))
00042